# enqueue(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Enqueues a buffer to the queue.

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
func enqueue(_ buffer: CMBuffer) throws
```

## Parameters

- `buffer`: The buffer to enqueue.

## See Also

### Managing a Queue
- [func dequeue() -> CMBuffer?](./dequeue%28%29.md)
  Dequeues a buffer from the queue.
- [func dequeueIfDataReady() -> CMBuffer?](./dequeueifdataready%28%29.md)
  Dequeues a buffer from the queue, if it’s ready.
- [func markEndOfData() throws](./markendofdata%28%29.md)
  Marks a buffer as being at the end of its data.
- [func reset() throws](./reset%28%29.md)
  Empties the queue and resets its end-of-data state.
- [func reset((CMBuffer) throws -> ()) throws](./reset%28_%29.md)
  Resets a buffer with a callback block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/enqueue(_:))*