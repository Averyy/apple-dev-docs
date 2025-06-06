# bufferCount

**Framework**: Core Media  
**Kind**: property

The count of buffers in the queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var bufferCount: CMItemCount { get }
```

## See Also

- [var isEmpty: Bool](cmbufferqueue/isempty.md)
  A Boolean value that indicates whether the queue contains buffers.
- [var head: CMBuffer?](cmbufferqueue/head.md)
  The element at the head of the queue.
- [var containsEndOfData: Bool](cmbufferqueue/containsendofdata.md)
  A Boolean value that indicates whether the buffer has its end-of-data state set.
- [var isAtEndOfData: Bool](cmbufferqueue/isatendofdata.md)
  A Boolean value that indicates whether that queue is at the end of its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/buffercount)*