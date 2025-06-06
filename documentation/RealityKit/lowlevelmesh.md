# LowLevelMesh

**Framework**: Realitykit  
**Kind**: class

A container for vertex data that you can use to create and update meshes using your own format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class LowLevelMesh
```

## Mentions

- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)

#### Overview

Use `LowLevelMesh` when you want to bring your own vertex format to RealityKit or update your data frequently. To update your data in `LowLevelMesh`, you can either use Swift for CPU processing, or Metal Compute Shaders for GPU processing.

> **Note**: Use [`MeshDescriptor`](meshdescriptor.md) for a simpler alternative to `LowLevelMesh`. For information on loading a model from a USD or Reality file, see [`Loading entities from a file`](loading-entities-from-a-file.md).

Express your vertex by creating a [`LowLevelMesh.Descriptor`](lowlevelmesh/descriptor-swift.struct.md) that describes your layout, along with the required index and vertex capacities. This descriptor is similar to [`MTLVertexDescriptor`](https://developer.apple.com/documentation/Metal/MTLVertexDescriptor), with additional semantics that make the data available in your shaders.

To use `LowLevelMesh`, first define your own vertex structure, either in a Metal header or using a Swift structure:

```swift
struct MyVertex {
    var position: SIMD3<Float> = .zero
    var color: UInt32 = .zero
}
```

Next, describe your structure to `LowLevelMesh` by creating a list of vertex attributes and a vertex layout. This description informs `LowLevelMesh` how to represent the vertex data in memory:

```swift
extension MyVertex {
    static var vertexAttributes: [LowLevelMesh.Attribute] = [
        .init(semantic: .position, format: .float3, offset: MemoryLayout<Self>.offset(of: \.position)!),
        .init(semantic: .color, format: .uchar4Normalized_bgra, offset: MemoryLayout<Self>.offset(of: \.color)!)
    ]

    static var vertexLayouts: [LowLevelMesh.Layout] = [
        .init(bufferIndex: 0, bufferStride: MemoryLayout<Self>.stride)
    ]

    static var descriptor: LowLevelMesh.Descriptor {
        var desc = LowLevelMesh.Descriptor()
        desc.vertexAttributes = MyVertex.vertexAttributes
        desc.vertexLayouts = MyVertex.vertexLayouts
        desc.indexType = .uint32
        return desc
    }
}
```

Create a [`LowLevelMesh.Descriptor`](lowlevelmesh/descriptor-swift.struct.md) and `LowLevelMesh`, and assign your mesh data and parts:

```swift
func triangleMesh() throws -> LowLevelMesh {
    var desc = MyVertex.descriptor
    desc.vertexCapacity = 3
    desc.indexCapacity = 3

    let mesh = try LowLevelMesh(descriptor: desc)

    mesh.withUnsafeMutableBytes(bufferIndex: 0) { rawBytes in
        let vertices = rawBytes.bindMemory(to: MyVertex.self)
        vertices[0] = MyVertex(position: [-1, -1, 0], color: 0xFF00FF00)
        vertices[1] = MyVertex(position: [ 1, -1, 0], color: 0xFFFF0000)
        vertices[2] = MyVertex(position: [ 0,  1, 0], color: 0xFF0000FF)
    }

    mesh.withUnsafeMutableIndices { rawIndices in
        let indices = rawIndices.bindMemory(to: UInt32.self)
        indices[0] = 0
        indices[1] = 1
        indices[2] = 2
    }

    let meshBounds = BoundingBox(min: [-1, -1, 0], max: [1, 1, 0])
    mesh.parts.replaceAll([
        LowLevelMesh.Part(
            indexCount: 3,
            topology: .triangle,
            bounds: meshBounds
        )
    ])

    return mesh
}
```

To finish, create a [`MeshResource`](meshresource.md) from the `LowLevelMesh`, and add it to a [`ModelComponent`](modelcomponent.md). You can then add this model to any [`Entity`](entity.md) in your scene:

```swift
func triangleEntity() throws -> Entity {
    let lowLevelMesh = try triangleMesh()
    let resource = try MeshResource(from: lowLevelMesh)

    let modelComponent = ModelComponent(mesh: resource, materials: [UnlitMaterial()])

    let entity = Entity()
    entity.name = "Triangle"
    entity.components.set(modelComponent)
    entity.scale *= 0.1
    return entity
}
```

The low-level mesh creates a triangular shape in your RealityKit scene:

![A screenshot of an isosceles triangle, floating in a kitchen scene. The triangle appears light gray in color.](https://docs-assets.developer.apple.com/published/53f5fd30d54e5aaa8c9b02f628ac1f48/lowlevelmesh-triangle-unlit.jpg)

The [`MeshResource`](meshresource.md) retains a reference to the `LowLevelMesh`, reflecting any changes when the renderer updates.

## Topics

### Creating a low-level mesh
- [init(descriptor: LowLevelMesh.Descriptor) throws](lowlevelmesh/init(descriptor:).md)
  Constructs a low-level mesh from a descriptor.
### Describing a low-level mesh
- [let descriptor: LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.property.md)
  The definition of the structure of this low-level mesh.
- [var parts: LowLevelMesh.PartsCollection](lowlevelmesh/parts.md)
  A mutable collection of parts.
- [var indexCapacity: Int](lowlevelmesh/indexcapacity.md)
  The capacity of the index buffer, measured in indices.
- [var vertexCapacity: Int](lowlevelmesh/vertexcapacity.md)
  The capacity of the vertex buffer, measured in vertices.
### Accessing mesh data on the CPU with Swift
- [func withUnsafeBytes(bufferIndex: Int, (UnsafeRawBufferPointer) -> Void)](lowlevelmesh/withunsafebytes(bufferindex:_:).md)
  Reads a Metal vertex buffer synchronously on the CPU.
- [func withUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/withunsafemutablebytes(bufferindex:_:).md)
  Updates a Metal vertex buffer synchronously on the CPU.
- [func withUnsafeIndices((UnsafeRawBufferPointer) -> Void)](lowlevelmesh/withunsafeindices(_:).md)
  Reads the index buffer synchronously on the CPU.
- [func withUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/withunsafemutableindices(_:).md)
  Updates the index buffer synchronously on the CPU.
- [func replaceUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/replaceunsafemutablebytes(bufferindex:_:).md)
  Replaces a Metal vertex buffer synchronously on the CPU.
- [func replaceUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/replaceunsafemutableindices(_:).md)
  Replaces the index buffer synchronously on the CPU.
### Accessing mesh data on the GPU with Metal
- [func read(bufferIndex: Int, using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelmesh/read(bufferindex:using:).md)
  Retrieves a Metal vertex buffer at the specified index, for GPU reading.
- [func readIndices(using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelmesh/readindices(using:).md)
  Retrieves the Metal index buffer for GPU reading.
- [func replace(bufferIndex: Int, using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelmesh/replace(bufferindex:using:).md)
  Retrieves a Metal vertex buffer you can use to replace the contents of the specified buffer on the GPU using Metal.
- [func replaceIndices(using: any MTLCommandBuffer) -> any MTLBuffer](lowlevelmesh/replaceindices(using:).md)
  Retrieves a Metal index buffer that you can use to replace the indices of this low-level mesh.
### Structures
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
### Enumerations
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/lowlevelmesh)*