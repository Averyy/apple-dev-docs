# init(vertexCapacity:vertexAttributes:vertexLayouts:indexCapacity:indexType:instanceCapacity:)

**Framework**: RealityKit  
**Kind**: init

Creates a mesh descriptor with the given vertex capacity, attributes, layouts, index capacity, index type, and instance capacity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(vertexCapacity: Int = 0, vertexAttributes: [LowLevelMeshResource.Attribute] = [Attribute](), vertexLayouts: [LowLevelMeshResource.Layout] = [Layout](), indexCapacity: Int = 0, indexType: MTLIndexType = MTLIndexType.uint32, instanceCapacity: Int = 0)
```

## Parameters

- `vertexCapacity`: The maximum number of vertices to allocate space for. Defaults to `0`.
- `vertexAttributes`: The vertex input attributes. Defaults to `[]`.
- `vertexLayouts`: The vertex buffer layouts. Defaults to `[]`.
- `indexCapacity`: The maximum number of indices to allocate space for. Defaults to `0`.
- `indexType`: The data type of the values stored in the index buffer. Defaults to `.uint32`.
- `instanceCapacity`: The maximum number of instances for per-instance vertex data. Defaults to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/descriptor-swift.struct/init(vertexcapacity:vertexattributes:vertexlayouts:indexcapacity:indextype:instancecapacity:))*