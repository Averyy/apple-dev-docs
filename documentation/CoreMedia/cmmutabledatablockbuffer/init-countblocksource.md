# init(count:blockSource:)

**Framework**: Core Media  
**Kind**: init

Creates a block buffer with `count` number of bytes.

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
init(count: Int = 0, blockSource: CMMutableDataBlockBuffer.BlockSource? = nil)
```

## Parameters

- `count`: Number of bytes to allocate in the block buffer.
- `blockSource`: Optional source to allocate and deallocate memory for the data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/init(count:blocksource:))*