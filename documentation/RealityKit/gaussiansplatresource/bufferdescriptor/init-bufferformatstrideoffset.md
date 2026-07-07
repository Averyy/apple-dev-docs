# init(buffer:format:stride:offset:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor that locates a property within a buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(buffer: LowLevelBuffer, format: MTLAttributeFormat, stride: Int, offset: Int)
```

## Parameters

- `buffer`: The buffer that stores the property’s values.
- `format`: The element format of each value in the buffer.
- `stride`: The distance, in bytes, between consecutive splats’ values.
- `offset`: The byte offset of the first splat’s value within the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferdescriptor/init(buffer:format:stride:offset:))*