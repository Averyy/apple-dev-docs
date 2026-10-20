# CMBufferQueueGetTotalSize(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern size_t CMBufferQueueGetTotalSize(CMBufferQueueRef queue);
```

#### Discussion

The total size of the `CMBufferQueue` is the sum of all the individual buffer sizes, as reported by the `getTotalSize` callback (provided to [`CMBufferQueueCreate(allocator:capacity:callbacks:queueOut:)`](./cmbufferqueuecreate%28allocator,capacity,callbacks,queueout%29.md)).

This function returns 0 if there are no buffers in the queue.

## See Also

### Inspecting a Queue
- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](./cmbufferqueueisempty%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](./cmbufferqueuegetbuffercount%28_%29.md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetHead(CMBufferQueue) -> CMBuffer?](./cmbufferqueuegethead%28_%29.md)
  Retrieves the next buffer from a queue, but doesn’t remove it.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](./cmbufferqueuecontainsendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](./cmbufferqueueisatendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegettotalsize(_:))*