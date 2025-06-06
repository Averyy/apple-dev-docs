# reset(_:)

**Framework**: Core Media  
**Kind**: method

Resets a buffer with a callback block.

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
func reset(_ body: (CMBuffer) throws -> ()) throws
```

## Parameters

- `body`: 

## See Also

- [func enqueue(CMBuffer) throws](cmbufferqueue/enqueue(_:).md)
  Enqueues a buffer to the queue.
- [func dequeue() -> CMBuffer?](cmbufferqueue/dequeue.md)
  Dequeues a buffer from the queue.
- [func dequeueIfDataReady() -> CMBuffer?](cmbufferqueue/dequeueifdataready.md)
  Dequeues a buffer from the queue, if it’s ready.
- [func markEndOfData() throws](cmbufferqueue/markendofdata.md)
  Marks a buffer as being at the end of its data.
- [func reset() throws](cmbufferqueue/reset.md)
  Empties the queue and resets its end-of-data state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/reset(_:))*