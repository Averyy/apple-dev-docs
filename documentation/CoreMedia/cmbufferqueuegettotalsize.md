# CMBufferQueueGetTotalSize(_:)

**Framework**: Core Media  
**Kind**: func

Gets the total size of all sample buffers of a buffer queue.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue) -> Int
```

#### Discussion

The total size of the `CMBufferQueue` is the sum of all the individual buffer sizes, as reported by the `getTotalSize` callback (provided to [`CMBufferQueueCreate(allocator:capacity:callbacks:queueOut:)`](cmbufferqueuecreate(allocator:capacity:callbacks:queueout:).md)).

This function returns 0 if there are no buffers in the queue.

## See Also

- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](cmbufferqueueisempty(_:).md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](cmbufferqueuegetbuffercount(_:).md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetHead(CMBufferQueue) -> CMBuffer?](cmbufferqueuegethead(_:).md)
  Retrieves the next buffer from a queue, but doesn’t remove it.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](cmbufferqueuecontainsendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](cmbufferqueueisatendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegettotalsize(_:))*