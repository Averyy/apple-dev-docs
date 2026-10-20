# CMBufferQueueGetHead(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves the next buffer from a queue, but doesn’t remove it.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0 (renamed: CMBufferQueueCopyHead(_:))
- iPadOS 4.0+ - Deprecated in 18.0 (renamed: CMBufferQueueCopyHead(_:))
- Mac Catalyst 13.1+ - Deprecated in 18.0 (renamed: CMBufferQueueCopyHead(_:))
- macOS 10.7+ - Deprecated in 15.0 (renamed: CMBufferQueueCopyHead(_:))
- tvOS 9.0+ - Deprecated in 18.0 (renamed: CMBufferQueueCopyHead(_:))
- visionOS 1.0+ - Deprecated in 2.0 (renamed: CMBufferQueueCopyHead(_:))
- watchOS 6.0+ - Deprecated in 11.0 (renamed: CMBufferQueueCopyHead(_:))

## Declaration

```swift
func CMBufferQueueGetHead(_ queue: CMBufferQueue) -> CMBuffer?
```

```c
extern CMBufferRefCMBufferQueueGetHead(CMBufferQueueRef queue);
```

#### Return Value

The buffer. Will be `NULL` if the queue is empty.

#### Discussion

This follows Core Foundation “Get” semantics – it does not retain the returned buffer. Note that with non-FIFO queues it’s not guaranteed that the next dequeue will return this particular buffer (if an intervening Enqueue adds a buffer that will dequeue next).

## Parameters

- `queue`: The CMBufferQueue from which to retrieve a buffer.

## See Also

### Inspecting a Queue
- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](./cmbufferqueueisempty%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](./cmbufferqueuegetbuffercount%28_%29.md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetTotalSize(CMBufferQueue) -> Int](./cmbufferqueuegettotalsize%28_%29.md)
  Gets the total size of all sample buffers of a buffer queue.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](./cmbufferqueuecontainsendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](./cmbufferqueueisatendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegethead(_:))*