# reset(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Resets a buffer with a callback block.

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
func reset(_ body: (CMBuffer) throws -> ()) throws
```

## Parameters

- `body`: 

## See Also

### Managing a Queue
- [func enqueue(CMBuffer) throws](./enqueue%28_%29.md)
  Enqueues a buffer to the queue.
- [func dequeue() -> CMBuffer?](./dequeue%28%29.md)
  Dequeues a buffer from the queue.
- [func dequeueIfDataReady() -> CMBuffer?](./dequeueifdataready%28%29.md)
  Dequeues a buffer from the queue, if it’s ready.
- [func markEndOfData() throws](./markendofdata%28%29.md)
  Marks a buffer as being at the end of its data.
- [func reset() throws](./reset%28%29.md)
  Empties the queue and resets its end-of-data state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/reset(_:))*