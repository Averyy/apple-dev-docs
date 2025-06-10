# Indexing Argument Buffers

**Framework**: Metal

Assign resource indices within an argument buffer.

#### Overview

You can index an argument buffer similarly to buffers, textures, and samplers. However, you index individual argument buffer resources with a generic `[[id(n)]]` attribute instead of the specific type `[[buffer(n)]]`, `[[texture(n)]]`, and `[[sampler(n)]]` attributes.

> **Note**:  Because argument buffers are represented by [`MTLBuffer`](mtlbuffer.md) objects, they can be explicitly distinguished from regular buffers in the Metal shading language if they contain any resources indexed with the `[[id(n)]]` attribute. If any member of a Metal shading language structure has an `[[id(n)]]` attribute, the whole structure is treated as an argument buffer.

Manually assigned argument buffer resource indices don’t need to be contiguous, but they must be unique and arranged in an increasing order. The following example shows manual and automatic index assignment:

```metal
struct My_Indexed_AB {
    texture2d<float> texA [[id(1)]];
    texture2d<float> texB [[id(3)]];
};
struct My_Aggregate_AB {
    My_Indexed_AB abX; // abX = id(0); texA = id(1); texB = id(3)
    My_Indexed_AB abY; // abY = id(4); texA = id(5); texB = id(7)
};
```

##### Automatically Assigned Index Ids

If the `[[id(n)]]` attribute is omitted for any argument buffer resource, an index ID is automatically assigned according to preset rules:

IDs are assigned to structure members in order, starting at 0, by adding 1 to the highest ID used by the previous structure member. The following example shows automatically assigned index IDs for structure members:

```metal
struct MaterialTexture {
    texture2d<float> tex; // Assigned to index 0
    float4 uvScaleOffset; // Assigned to index 1
};
```

IDs are assigned to array elements in order, starting at 0, by adding 1 to the highest ID used by the previous array elements. The following example shows automatically assigned index IDs for array elements:

```metal
struct Material {
    float4 diffuse;                     // Assigned to index 0
    array<texture2d<float>, 3> texSet1; // Assigned to indices 1-3
    texture2d<float> texSet2[3];        // Assigned to indices 4-6
    MaterialTexture materials[3];       // Assigned to indices 7-12
    int constants[4] [[id(20)]];        // Assigned to indices 20-23
};
```

If a structure member or array element is itself a structure or array, its own structure members or array elements are assigned indices according to the previous rules. If an ID is provided for a top-level structure or array, this ID becomes the starting index for nested structure members or array elements. The following example shows automatically assigned index IDs for nested structures and arrays:

```metal
struct Material {
    MaterialTexture diffuse;          // Assigned to indices 0-1
    MaterialTexture normal [[id(4)]]; // Assigned to indices 4-5
    MaterialTexture specular;         // Assigned to indices 6-7
}
```

Argument buffer resources are assigned generic indices according to the previous rules. Regular resources are assigned type indices in their respective resource argument tables. The following example shows automatically assigned index IDs for combined argument buffer resources and regular resources:

```metal
fragment float4 my_fragment(
    constant texture2d<float> & texturesAB1 [[buffer(0)]],     // Assigned to generic index 0 and buffer index 0
    constant texture2d<float> & texturesAB2[10] [[buffer(1)]], // Assigned to generic indices 0-9 and buffer index 1
    array<texture2d<float>, 10> texturesArray [[texture(0)]]    // Assigned to texture indices 0-9
)
{...}
```

## See Also

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Rendering Terrain Dynamically with Argument Buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding Argument Buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An object used to encode data into an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/indexing-argument-buffers)*