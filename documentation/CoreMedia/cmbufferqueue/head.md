# head

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The element at the head of the queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var head: CMBuffer? { get }
```

## See Also

### Inspecting a Queue
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the queue contains buffers.
- [var bufferCount: CMItemCount](./buffercount.md)
  The count of buffers in the queue.
- [var containsEndOfData: Bool](./containsendofdata.md)
  A Boolean value that indicates whether the buffer has its end-of-data state set.
- [var isAtEndOfData: Bool](./isatendofdata.md)
  A Boolean value that indicates whether that queue is at the end of its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/head)*