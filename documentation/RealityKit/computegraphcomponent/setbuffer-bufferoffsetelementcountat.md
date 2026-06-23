# setBuffer(_:bufferOffset:elementCount:at:)

**Framework**: RealityKit  
**Kind**: method

Binds a Metal buffer to a parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func setBuffer(_ buffer: (any MTLBuffer)?, bufferOffset: Int = 0, elementCount: Int? = nil, at index: Int)
```

## Parameters

- `buffer`: The `MTLBuffer` to bind.
- `bufferOffset`: Byte offset into `buffer`. Defaults to `0`.
- `elementCount`: Number of elements in the buffer, for buffers with variable capacity.
- `at`: Index into the device buffers table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/setbuffer(_:bufferoffset:elementcount:at:))*