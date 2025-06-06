# fill(_:offset:)

**Framework**: Model I/O  
**Kind**: method  
**Required**: Yes

Writes the specified data into the buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func fill(_ data: Data, offset: Int)
```

#### Discussion

If the length of the specified data (plus the `offset` parameter, if nonzero) is greater than the buffer’s [`length`](mdlmeshbuffer/length.md) property, this method writes data only up to the end of the buffer.

## Parameters

- `data`: The data to be copied into the buffer.
- `offset`: The offset, in bytes, from the start of the buffer at which to write data.

## See Also

- [func map() -> MDLMeshBufferMap](mdlmeshbuffer/map.md)
  Provides direct, read-only access to the buffer’s contents.
- [var length: Int](mdlmeshbuffer/length.md)
  The data size of the buffer, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/fill(_:offset:))*