# init(subBlockCapacity:blockSource:)

**Framework**: Core Media  
**Kind**: init

Creates a block buffer with at least `subBlockCapacity` number of sub blocks.

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
init(subBlockCapacity: Int, blockSource: CMMutableDataBlockBuffer.BlockSource? = nil)
```

## Parameters

- `subBlockCapacity`: Number of sub-blocks the new block buffer shall accommodate before expansion   occurs. A value of zero means “do the reasonable default”.
- `blockSource`: Optional source to allocate and deallocate memory for the data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/init(subblockcapacity:blocksource:))*