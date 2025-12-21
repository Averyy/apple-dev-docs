# Creating a plane with low-level mesh

**Framework**: RealityKit

Create a low-level mesh and set its vertex positions and normals to form a plane.

#### Overview

A plane mesh is an excellent starting point for a variety of interactive applications, such as a cloth or water simulation. However, to achieve these dynamic effects you need to modify the mesh’s vertices in every frame, which is inefficient without direct access to the underlying GPU buffers. [`LowLevelMesh`](lowlevelmesh.md) addresses this inefficiency by allowing you to create a custom vertex format and vertex buffer layout, which you can update in real time on the GPU by dispatching Metal compute shaders.

Construct a plane mesh by defining a custom vertex structure and creating a [`LowLevelMesh`](lowlevelmesh.md) with enough vertex and index capacity to store the vertices. Position the vertices of the mesh in the shape of a plane by filling in the index and vertex buffers with data. See [`Generating interactive geometry with RealityKit`](generating-interactive-geometry-with-realitykit.md) for further applications of this mesh, including a terrain editor and water simulation.

#### Define a Custom Vertex Structure

Start by defining a custom vertex structure in a [`Metal Shading Language`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) header file:

```cpp
struct PlaneVertex {
    simd_float3 position;
    simd_float3 normal;
};
```

In this example, the vertex has a 3D position and a 3D normal vector, but you can further customize your vertex structure with different names and additional data, such as color and UV data.

Make `PlaneVertex` accessible in both Swift files and Metal files by referencing it in a bridging file. See [`Passing Structured Data to a Metal Compute Function`](passing-structured-data-to-a-metal-compute-function#Import-the-struct-in-a-bridging-header.md) for more information about bridging files.

#### Define a Plane Mesh Structure

Define a structure that constructs the plane low-level mesh with size and dimensions:

```swift
struct PlaneMesh {
    /// The plane low-level mesh.
    var mesh: LowLevelMesh!
    /// The size of the plane mesh.
    let size: SIMD2<Float>
    /// The number of vertices in each dimension of the plane mesh.
    let dimensions: SIMD2<UInt32>
    /// The maximum offset depth for the vertices of the plane mesh.
    ///
    /// Use this to ensure the bounds of the plane encompass its vertices, even if they are offset.
    let maxVertexDepth: Float
    
    ...
    
    /// Initializes the plane mesh by creating a low-level mesh and filling its vertex and index buffers
    /// to form a plane with given size and dimensions.
    init(size: SIMD2<Float>, dimensions: SIMD2<UInt32>, maxVertexDepth: Float = 1) throws {
        self.size = size
        self.dimensions = dimensions
        self.maxVertexDepth = maxVertexDepth
        
        // Create the low-level mesh.
        self.mesh = try createMesh()

        // Fill the mesh's vertex buffer with data.
        initializeVertexData()
        
        // Fill the mesh's index buffer with data.
        initializeIndexData()
        
        // Initialize the mesh parts.
        initializeMeshParts()
    }
}
```

See the following sections for the implementation details of each of the methods in the structure’s initializer.

#### Create the Low Level Mesh

Start by specifying the layout of the vertex data with a [`LowLevelMesh.Attribute`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/lowlevelmesh/attribute) array and a [`LowLevelMesh.Layout`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/lowlevelmesh/layout) array:

```swift
/// Creates a low-level mesh with `PlaneVertex` vertices.
private func createMesh() throws -> LowLevelMesh {
    // Define the vertex attributes of `PlaneVertex`.
    let positionAttributeOffset = MemoryLayout.offset(of: \PlaneVertex.position) ?? 0
    let normalAttributeOffset = MemoryLayout.offset(of: \PlaneVertex.normal) ?? 16
    
    let positionAttribute = LowLevelMesh.Attribute(semantic: .position, format: .float3, offset: positionAttributeOffset)
    let normalAttribute = LowLevelMesh.Attribute(semantic: .normal, format: .float3, offset: normalAttributeOffset)
    
    let vertexAttributes = [positionAttribute, normalAttribute]
    
    // Define the vertex layouts of `PlaneVertex`.
    let vertexLayouts = [LowLevelMesh.Layout(bufferIndex: 0, bufferStride: MemoryLayout<PlaneVertex>.stride)]
```

These arrays define which properties in your custom vertex structure represent the different components of the vertex, such as position, normal, color, and so on, as well as their memory layout.

Next, derive the number of vertices and indices in the mesh from its dimensions:

```swift
    // Derive the vertex and index count from the dimensions.
    let vertexCount = Int(dimensions.x * dimensions.y)
    let indicesPerTriangle = 3
    let trianglesPerCell = 2
    let cellCount = Int((dimensions.x - 1) * (dimensions.y - 1))
    let indexCount = indicesPerTriangle * trianglesPerCell * cellCount
```

Finally, create the low-level mesh by describing its vertex capacity, attributes, layouts, and index capacity:

```swift
    // Create a low-level mesh with the necessary `PlaneVertex` capacity.
    let meshDescriptor = LowLevelMesh.Descriptor(vertexCapacity: vertexCount,
                                                 vertexAttributes: vertexAttributes,
                                                 vertexLayouts: vertexLayouts,
                                                 indexCapacity: indexCount)
    return try LowLevelMesh(descriptor: meshDescriptor)
}
```

#### Initialize the Data in the Meshs Vertex and Index Buffers

Prepare the mesh for rendering by filling in its vertex and index buffers with data on the CPU, as in the following image:

![A screenshot of a wireframe rendering of the plane mesh with 16 vertices in each dimension, floating in a kitchen scene. Lines connect the vertices to form 512 triangles.](https://docs-assets.developer.apple.com/published/687b1928fabe0483380ad3d7ebe60f70/creating-a-plane-with-low-level-mesh-1.jpg)

> **Note**: You can also fill in the data on the GPU by running a Metal compute shader (see [`Generating interactive geometry with RealityKit`](generating-interactive-geometry-with-realitykit.md)).

Start by defining a helper method that converts a two-dimensional vertex coordinate to a one-dimensional vertex buffer array index:

```swift
/// Converts a 2D vertex coordinate to a 1D vertex buffer index.
private func vertexIndex(_ xCoord: UInt32, _ yCoord: UInt32) -> UInt32 {
    xCoord + dimensions.x * yCoord
}
```

Next, initialize the vertices of the low-level mesh by setting their normal directions and positioning them to form a plane with the given size:

```swift
/// Initialize the vertices of the mesh, positioning them to form an xy-plane with the given size.
private func initializeVertexData() {
    // Initialize mesh vertex positions and normals.
    mesh.withUnsafeMutableBytes(bufferIndex: 0) { rawBytes in
        // Convert `rawBytes` into a `PlaneVertex` buffer pointer.
        let vertices = rawBytes.bindMemory(to: PlaneVertex.self)
        
        // Define the normal direction for the vertices.
        let normalDirection: SIMD3<Float> = [0, 0, 1]

        // Iterate through each vertex.
        for xCoord in 0..<dimensions.x {
            for yCoord in 0..<dimensions.y {
                // Remap the x and y vertex coordinates to the range [0, 1].
                let xCoord01 = Float(xCoord) / Float(dimensions.x - 1)
                let yCoord01 = Float(yCoord) / Float(dimensions.y - 1)
                
                // Derive the vertex position from the remapped vertex coordinates and the size.
                let xPosition = size.x * xCoord01 - size.x / 2
                let yPosition = size.y * yCoord01 - size.y / 2
                let zPosition = Float(0)
                
                // Get the current vertex from the vertex coordinates and set its position and normal.
                let vertexIndex = Int(vertexIndex(xCoord, yCoord))
                vertices[vertexIndex].position = [xPosition, yPosition, zPosition]
                vertices[vertexIndex].normal = normalDirection
            }
        }
    }
}
```

Loop over the vertices within the [`withUnsafeMutableBytes`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/lowlevelmesh/withunsafemutablebytes(bufferindex:_:)) callback for best performance, as calling this method repeatedly is costly.

Finally, fill the index buffer by iterating through each cell in the mesh and adding the vertices of the two triangles that make up the cell in a counterclockwise winding order:

```swift
/// Initializes the indices of the mesh two triangles at a time for each cell in the mesh.
private func initializeIndexData() {
    mesh.withUnsafeMutableIndices { rawIndices in
        // Convert `rawIndices` into a UInt32 pointer.
        guard var indices = rawIndices.baseAddress?.assumingMemoryBound(to: UInt32.self) else { return }
        
        // Iterate through each cell.
        for xCoord in 0..<dimensions.x - 1 {
            for yCoord in 0..<dimensions.y - 1 {
                /*
                   Each cell in the plane mesh consists of two triangles:
                    
                              topLeft     topRight
                                     |\ ̅ ̅|
                     1st Triangle--> | \ | <-- 2nd Triangle
                                     | ̲ ̲\|
                  +y       bottomLeft     bottomRight
                   ^
                   |
                   *---> +x
                 
                 */
                let bottomLeft = vertexIndex(xCoord, yCoord)
                let bottomRight = vertexIndex(xCoord + 1, yCoord)
                let topLeft = vertexIndex(xCoord, yCoord + 1)
                let topRight = vertexIndex(xCoord + 1, yCoord + 1)
                
                // Create the 1st triangle with a counterclockwise winding order.
                indices[0] = bottomLeft
                indices[1] = bottomRight
                indices[2] = topLeft
                
                // Create the 2nd triangle with a counterclockwise winding order.
                indices[3] = topLeft
                indices[4] = bottomRight
                indices[5] = topRight
                
                indices += 6
            }
        }
    }
}
```

Loop over the indices within the [`withUnsafeMutableIndices`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/lowlevelmesh/withunsafemutableindices(_:)) callback for best performance.

> **Note**: The winding order of the vertices in a triangle determine which side of the triangle is the front. RealityKit considers a counterclockwise winding order to be front-facing.

#### Initialize the Mesh Parts

Initialize the mesh parts by specifying the mesh’s index count, topology, and bounds:

```swift
/// Initializes mesh parts, indicating topology and bounds.
func initializeMeshParts() {
    // Create a bounding box that encompasses the plane's size and max vertex depth.
    let bounds = BoundingBox(min: [-size.x / 2, -size.y / 2, 0],
                             max: [size.x / 2, size.y / 2, maxVertexDepth])
    
    mesh.parts.replaceAll([LowLevelMesh.Part(indexCount: mesh.descriptor.indexCapacity,
                                             topology: .triangle,
                                             bounds: bounds)])
}
```

In this example, the `maxVertexDepth` property specifies the maximum offset depth for the vertices. The mesh’s bounding box relies on this value to ensure it will encompass the vertices at all times, even if they are offset from their original positions.

> **Note**: RealityKit uses `bounds` to determine whether or not to cull an object during rendering. Therefore, it’s essential that the bounds you define are large enough to contain all of the vertices of your mesh; otherwise, RealityKit may not render it correctly.

#### Create an Entity with the Low Level Mesh

View `PlaneMesh`’s low-level mesh by creating a [`MeshResource`](meshresource.md) from it and adding that to the [`ModelComponent`](modelcomponent.md) of an entity in the scene:

```swift
RealityView { content in
    // Create a plane mesh.
    if let planeMesh = try? PlaneMesh(size: [1, 1], dimensions: [16, 16]),
       let mesh = try? MeshResource(from: planeMesh.mesh) {
        // Create an entity with the plane mesh.
        let planeEntity = Entity()
        let planeModel = ModelComponent(mesh: mesh, materials: [SimpleMaterial()])
        planeEntity.components.set(planeModel)
        
        // Add the plane entity to the scene.
        content.add(planeEntity)
    }
}
```

The following image shows the result of rendering a `PlaneMesh`’s low-level mesh in the scene:

![A screenshot of a flat plane mesh floating in a kitchen scene. The plane appears light gray.](https://docs-assets.developer.apple.com/published/b5ffd7673f3a52999377fc9bb30a4fd1/creating-a-plane-with-low-level-mesh-2.jpg)

## See Also

- [Integrating virtual objects with your environment](integrating-virtual-objects-with-your-environment.md)
  Create an immersive game using native anchor support, environmental blending, model manipulation, and mesh instance duplication.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](lowlevelbuffer.md)
- [class LowLevelInstanceData](lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/creating-a-plane-with-low-level-mesh)*