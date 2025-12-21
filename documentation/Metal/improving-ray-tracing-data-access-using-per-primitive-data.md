# Improving ray-tracing data access using per-primitive data

**Framework**: Metal

Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.

#### Overview

Creating a ray-traced renderer — or using ray tracing to implement other behaviors — requires more than simple geometry. Your app also needs to provide custom data to your ray-tracing kernels. For example, a renderer might need UV coordinates and textures, as well as colors and other material properties, to calculate proper reflections and lighting. Some ray tracers use those same elements to implement other behaviors. For example, you can use an alpha texture and a texture lookup to implement opacity in a custom intersection function. How you organize your custom data can affect both the readability and performance of your ray-tracing kernels.

Consider the figure below, which describes one possible way to organize your app’s data. A material consists of multiple pieces of data, stored as textures and constants, that the renderer uses to compute lighting and shading. Each primitive in the geometry can have a different material applied to it. To avoid duplicating material data, the app stores a single copy of each material in a Metal buffer, and stores a material ID for each primitive in a second Metal buffer. A third Metal buffer contains UV data for each primitive. A shader or kernel that uses this data arrangement needs to first fetch the material ID and UV coordinates using the primitive index, and then use the material ID to look up the material data. A more complicated renderer could go a step further for multiple instances of the geometry, using another buffer to hold instanced data.

![A block diagram showing how an intersection function traces through intermediate data structures to retrieve the data it needs to perform an intersection test. The diagram shows three Metal buffers, containing UV coordinates for each primitive, material IDs for each primitive, and material data for each material. The intersection function uses the primitive ID to retrieve the appropriate material ID and UV coordinates, and then uses the material ID to retrieve the material data.](https://docs-assets.developer.apple.com/published/b2dc5e73008f5479b19579d98d8d0224/media-4452905%402x.png)

Retrieving the data needed to calculate the result requires the kernel to dereference multiple pointers, and to store more intermediate variables. In a complex renderer, the performance penalties for this might be small. On the other hand, when you run an intersector using primitives with custom intersection functions, the intersector might execute multiple intersection tests for each ray. Such functions are often much simpler than shaders, so the penalty for dereferencing additional pointers might be a larger part of the total time executing the kernel.

For better Metal performance, copy primitive data into the acceleration structures and access it directly in your shaders. Using per-primitive data simplifies your shaders and make them easier to read, and you avoid needing to perform a separate data lookup based on the primitive ID. It also reduces the cost of transversing your data while simultaneously reducing GPU overhead. For kernels or functions that you run frequently on the GPU, or functions that contain many memory operations, use per-primitive data to improve performance.

##### Create a Data Type for the Primitive Data

Start by defining a structure for your per-primitive data in a file that your project shares between the app’s CPU and shader code. For example, you could define the data structure in the same place where you define the parameter types for your shaders and compute kernels:

```objective-c
#include <simd/simd.h>

struct PrimitiveTextureData {
    uint64_t textureAddress;
    vector_float2 coordinates[3];
};

struct TriangleData {
    vector_float3 normal0;
    vector_float3 normal1;
    vector_float3 normal2;

    vector_float3 color0;
    vector_float3 color1;
    vector_float3 color2;
};
```

A per-primitive data type can store the same types as an argument buffer (see [`Improving CPU performance by using argument buffers`](improving-cpu-performance-by-using-argument-buffers.md)), including basic scalar types, vector types, and references to Metal resources. Metal doesn’t limit the size of per-primitive data structures, but acceleration structures with large primitive data may need significantly more memory and take longer to create, copy, and refit. The additional data may also affect your shaders’ performance at runtime. For best results, limit the data to values that are the same across multiple instances of the geometry, and store only those values needed to perform the most frequent or expensive tasks.

> 💡 **Tip**:  Profile your app before and after you make any changes to how you store your data so that you can measure the benefit you gained from the changes.

One way to reduce a per-primitive structure’s size is by including a pointer to another buffer. Although this approach brings back some of the complexity of the earlier buffered approach, it still provides relatively quick access to data in the secondary structure. Put the data that you need most in the per-primitive structure, and access the secondary structure only when necessary. For better cache performance, pack both structures so that you store values you access at the same time near each other in memory.

##### Add the Per Primitive Data to Your Acceleration Structure

You add the primitive data to your acceleration structure by including it when you create the acceleration structure. Start by copying the data for the primitives into an [`MTLBuffer`](mtlbuffer.md) instance. Each primitive needs its own instance of the primitive data, stored in linear order.

When you configure the geometry descriptor, set the [`primitiveDataBuffer`](mtlaccelerationstructuregeometrydescriptor/primitivedatabuffer.md) property to point to this buffer. If the data doesn’t start at the beginning of the buffer, set the [`primitiveDataBufferOffset`](mtlaccelerationstructuregeometrydescriptor/primitivedatabufferoffset.md) to the location of the first byte of per-primitive data within the buffer.

Next, set the [`primitiveDataElementSize`](mtlaccelerationstructuregeometrydescriptor/primitivedataelementsize.md) property to the size of your primitive data structure, and the [`primitiveDataStride`](mtlaccelerationstructuregeometrydescriptor/primitivedatastride.md) property to the number of bytes between two consecutive instances of the per-primitive data in the buffer. The stride property defaults to `0`, which tells Metal the buffer’s stride is the same as the element size.

The [`MTLAccelerationStructureGeometryDescriptor`](mtlaccelerationstructuregeometrydescriptor.md) type defines these properties for its subclasses, which include the following descriptor types:

- [`MTLAccelerationStructureTriangleGeometryDescriptor`](mtlaccelerationstructuretrianglegeometrydescriptor.md)
- [`MTLAccelerationStructureMotionTriangleGeometryDescriptor`](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
- [`MTLAccelerationStructureCurveGeometryDescriptor`](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [`MTLAccelerationStructureMotionCurveGeometryDescriptor`](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [`MTLAccelerationStructureBoundingBoxGeometryDescriptor`](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
- [`MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor`](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)

In the example below, the method configures per-primitive data for a triangle geometry descriptor with a buffer that contains one instance of the primitive data for each triangle.

```swift
func configure(geometryDescriptor: MTLAccelerationStructureTriangleGeometryDescriptor,
               with trianglePrimitiveData: MTLBuffer) {
    geometryDescriptor.primitiveDataBuffer = trianglePrimitiveData
    geometryDescriptor.primitiveDataBufferOffset = 0
    geometryDescriptor.primitiveDataElementSize = MemoryLayout<PrimitiveTextureData>.size
    geometryDescriptor.primitiveDataStride = MemoryLayout<PrimitiveTextureData>.stride
}
```

When you create the acceleration structure, Metal copies the data from the primitive data buffer into the new structure. Afterward, you can delete the primitive data buffer if you don’t have another use for it.

##### Access the Per Primitive Data Within a Ray Tracing Kernel

When your ray-tracing kernel calls an intersect method, Metal includes the primitive data for any intersected primitive in the intersection result. Retrieve the data for the primitive by accessing the `primitive_data` field:

```metal
/// The GPU invokes this kernel for each ray it casts into the scene.
kernel void rayTracingKernel(uint2 threadID [[thread_position_in_grid]],
// ...
                             instance_acceleration_structure accelerationStructure [[buffer(4)]],
                             intersection_function_table<triangle_data, instancing> intersectionFunctionTable [[buffer(5)]]
                             )
{
    /// Represents a single ray for a ray-tracing scene.
    ray ray;

    /// An intersector that tests for intersections between the ray and the geometry in the scene.
    intersector<triangle_data, instancing> triangleIntersector;

    /// The result value type that represents an intersection with the scene's geometry.
    intersector<triangle_data, instancing>::result_type result;

    ...

    // Test the ray for intersection with an acceleration structure's geometry.
    result = triangleIntersector.intersect(ray, accelerationStructure);

    if (result.type != intersection_type::none) {
        const device PrimitiveTextureData *textureData;

        // Retrieve the data that's specific to the triangle the ray intersects.
        textureData = (const device PrimitiveTextureData *) result.primitive_data;

        vector_float2 uv = textureData->coordinates;
        uint64_t texture = textureData->textureAddress;

        ...
    }
}
```

If your implementation uses an intersection function, access the candidate’s primitive data by adding a parameter with the `[[primitive_data]]` attribute:

```metal
/// The intersection function for the triangle's kernel.
[[intersection(triangle)]]
bool triangle_intersection_function(const device PrimitiveTextureData *textureData [[primitive_data]]
                                    ... ) {
    ...

    return true;
}
```

Finally, if your implementation uses intersection queries, access a primitive’s data by calling the query’s `get_candidate_primitive_data()` and `get_committed_primitive_data()` methods.

```metal
intersection_query<triangle_data, instancing> query;

const device PrimitiveTextureData* candidatePrimitiveData;
const device PrimitiveTextureData* committedPrimitiveData;

...

candidatePrimitiveData = (const device PrimitiveTextureData *) query.get_candidate_primitive_data();

...

committedPrimitiveData = (const device PrimitiveTextureData *) query.get_committed_primitive_data();
```

> 💡 **Tip**:  Improve the runtime performance of your Metal apps that use intersection queries by converting to an implementation that uses kernels with intersectors, with or without custom intersection functions.

## See Also

- [protocol MTLAccelerationStructure](mtlaccelerationstructure.md)
  A collection of model data for GPU-accelerated intersection of rays with the model.
- [class MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)
  Base class for Metal 4 acceleration structure descriptors.
- [class MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)
  A base class for classes that define the configuration for a new acceleration structure.
- [class MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md)
  Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [class MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md)
  A description of an acceleration structure that contains geometry primitives.
- [class MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md)
  Descriptor for an instance acceleration structure.
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  Encodes commands that build and refit acceleration structures for a single pass.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/improving-ray-tracing-data-access-using-per-primitive-data)*