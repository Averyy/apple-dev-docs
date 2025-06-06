# CMBufferQueueIsEmpty(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a buffer queue is empty.

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
func CMBufferQueueIsEmpty(_ queue: CMBufferQueue) -> Bool
```

#### Return Value

A Boolean indicating whether the `CMBufferQueue` is empty. If queue is `NULL`, true is returned.

## Parameters

- `queue`: The   being interrogated.

## See Also

- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](cmbufferqueuegetbuffercount(_:).md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetTotalSize(CMBufferQueue) -> Int](cmbufferqueuegettotalsize(_:).md)
  Gets the total size of all sample buffers of a buffer queue.
- [func CMBufferQueueGetHead(CMBufferQueue) -> CMBuffer?](cmbufferqueuegethead(_:).md)
  Retrieves the next buffer from a queue, but doesn’t remove it.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](cmbufferqueuecontainsendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](cmbufferqueueisatendofdata(_:).md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueueisempty(_:))*