# makeBlockBuffer(copying:)

**Framework**: Core Media  
**Kind**: method

Creates a block buffer by copying the given audio buffer list.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final func makeBlockBuffer(copying audioBuffers: UnsafePointer<AudioBufferList>) -> CMMutableDataBlockBuffer
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/memorypool/makeblockbuffer(copying:))*