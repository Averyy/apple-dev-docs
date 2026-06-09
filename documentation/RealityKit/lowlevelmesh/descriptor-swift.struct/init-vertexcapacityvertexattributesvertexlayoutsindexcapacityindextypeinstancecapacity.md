# init(vertexCapacity:vertexAttributes:vertexLayouts:indexCapacity:indexType:instanceCapacity:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor for a low-level mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(vertexCapacity: Int = 0, vertexAttributes: [LowLevelMesh.Attribute] = [Attribute](), vertexLayouts: [LowLevelMesh.Layout] = [Layout](), indexCapacity: Int = 0, indexType: MTLIndexType = MTLIndexType.uint32, instanceCapacity: Int = 0)
```

#### Discussion

To create a new [`LowLevelMesh`](lowlevelmesh.md), first create a `Descriptor` object and set its property values, then use that `Descriptor` with [`init(descriptor:)`](lowlevelmesh/init(descriptor:).md).

## Parameters

- `vertexCapacity`: The maximum number of vertices the system can store in the mesh.
- `vertexAttributes`: The attributes of the vertices.
- `vertexLayouts`: The layouts for the vertex buffers.
- `indexCapacity`: The maximum number of vertices the system can store in a single buffer.
- `indexType`: The index type to use for the mesh.
- `instanceCapacity`: The maximum number of instances the mesh supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/init(vertexcapacity:vertexattributes:vertexlayouts:indexcapacity:indextype:instancecapacity:))*