# init(semantic:format:layoutIndex:offset:)

**Framework**: RealityKit  
**Kind**: init

Creates an attribute with the given semantic, format, layout index, and byte offset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(semantic: LowLevelMeshResource.VertexSemantic, format: MTLVertexFormat, layoutIndex: Int = 0, offset: Int)
```

## Parameters

- `semantic`: The semantic describing how the renderer interprets this attribute.
- `format`: The Metal vertex format of the attribute.
- `layoutIndex`: The index of the layout that contains this attribute. Defaults to `0`.
- `offset`: The byte offset of this attribute from the start of the vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/attribute/init(semantic:format:layoutindex:offset:))*