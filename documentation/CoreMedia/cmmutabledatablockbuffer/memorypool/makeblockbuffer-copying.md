# makeBlockBuffer(copying:)

**Framework**: Core Media  
**Kind**: method

Creates a block buffer by copying the given audio buffer list.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func makeBlockBuffer(copying audioBuffers: UnsafePointer<AudioBufferList>) -> CMMutableDataBlockBuffer
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/memorypool/makeblockbuffer(copying:))*