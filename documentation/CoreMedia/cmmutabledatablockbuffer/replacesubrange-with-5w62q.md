# replaceSubrange(_:with:)

**Framework**: Core Media  
**Kind**: method

Replace a range of bytes in the block buffer.

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
mutating func replaceSubrange(_ range: Range<Int>, with bytes: some DataProtocol)
```

#### Discussion

This function also works if the range covers non-contiguous regions of memory.

## Parameters

- `range`: Range of bytes to replace within this buffer. The count of this range must match the count of  .
- `bytes`: The replacement data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/replacesubrange(_:with:)-5w62q)*