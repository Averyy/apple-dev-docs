# setBuffer(_:bufferOffset:elementCount:at:)

**Framework**: RealityKit  
**Kind**: method

Binds a Metal buffer to a parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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