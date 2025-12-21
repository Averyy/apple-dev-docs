# init(copying:blockSource:)

**Framework**: Core Media  
**Kind**: init

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
init(copying audioBuffers: UnsafePointer<AudioBufferList>, blockSource: CMMutableDataBlockBuffer.BlockSource? = nil)
```

## Parameters

- `audioBuffers`: Audio buffer list to copy into the new block buffer.
- `blockSource`: Optional source to allocate and deallocate memory for the data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/init(copying:blocksource:))*