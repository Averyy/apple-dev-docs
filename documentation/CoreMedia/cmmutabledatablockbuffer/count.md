# count

**Framework**: Core Media  
**Kind**: property

The number of bytes in the block buffer.

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
var count: Int { get }
```

#### Discussion

This count is the sum of the number of bytes in each memory block and buffer reference held in the block buffer. Note that the buffer references may hold more data than referenced by this block buffer. This block buffer presents a contiguous range of offsets from 0 to `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/count)*