# map()

**Framework**: Model I/O  
**Kind**: method  
**Required**: Yes

Provides direct, read-only access to the buffer’s contents.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func map() -> MDLMeshBufferMap
```

#### Return Value

A data object mapped to the storage memory for the buffer.

#### Discussion

The buffer’s storage remains mapped for as long as the returned [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object exists, potentially restricting other uses of that storage. For example, if a buffer’s storage is shared with GPU memory, that buffer may be unavailable for use in rendering until the [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object is deallocated.

## See Also

- [func fill(Data, offset: Int)](mdlmeshbuffer/fill(_:offset:).md)
  Writes the specified data into the buffer.
- [var length: Int](mdlmeshbuffer/length.md)
  The data size of the buffer, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/map())*