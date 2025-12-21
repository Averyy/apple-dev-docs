# isContiguous

**Framework**: Core Media  
**Kind**: property

Determine whether the block buffer is contiguous.

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
var isContiguous: Bool { get }
```

#### Discussion

`true` if block buffer references a single contiguous memory block `false` otherwise. Also `false` if the buffer is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/iscontiguous)*