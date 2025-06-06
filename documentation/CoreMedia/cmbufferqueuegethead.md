# CMBufferQueueGetHead(_:)

**Framework**: Core Media  
**Kind**: func

Retrieves the next buffer from a queue, but doesn’t remove it.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueGetHead(_ queue: CMBufferQueue) -> CMBuffer?
```

#### Return Value

The buffer. Will be `NULL` if the queue is empty.

#### Discussion

This follows Core Foundation “Get” semantics – it does not retain the returned buffer. Note that with non-FIFO queues it’s not guaranteed that the next dequeue will return this particular buffer (if an intervening Enqueue adds a buffer that will dequeue next).

## Parameters

- `queue`: The CMBufferQueue from which to retrieve a buffer.

## See Also

- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](cmbufferqueueisempty(_:).md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](cmbufferqueuegetbuffercount(_:).md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetTotalSize(CMBufferQueue) -> Int](cmbufferqueuegettotalsize(_:).md)
  Gets the total size of all sample buffers of a buffer queue.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](cmbufferqueuecontainsendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](cmbufferqueueisatendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegethead(_:))*