# replaceSubrange(_:with:)

**Framework**: Core Media  
**Kind**: method

Replace a range of bytes in the block buffer.

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
mutating func replaceSubrange(_ range: Range<Int>, with bytes: some DataProtocol)
```

#### Discussion

This function also works if the range covers non-contiguous regions of memory.

## Parameters

- `range`: Range of bytes to replace within this buffer. The count of this range must match the count of  .
- `bytes`: The replacement data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/replacesubrange(_:with:)-5w62q)*