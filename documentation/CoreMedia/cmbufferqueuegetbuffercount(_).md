# CMBufferQueueGetBufferCount(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the number of buffers in the queue.

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
func CMBufferQueueGetBufferCount(_ queue: CMBufferQueue) -> CMItemCount
```

```c
extern CMItemCount CMBufferQueueGetBufferCount(CMBufferQueueRef queue);
```

#### Return Value

Returns the number of buffers in the `CMBufferQueue`.

## Parameters

- `queue`: `CMBufferQueue` being interrogated.

## See Also

### Inspecting a Queue
- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](./cmbufferqueueisempty%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetTotalSize(CMBufferQueue) -> Int](./cmbufferqueuegettotalsize%28_%29.md)
  Gets the total size of all sample buffers of a buffer queue.
- [func CMBufferQueueGetHead(CMBufferQueue) -> CMBuffer?](./cmbufferqueuegethead%28_%29.md)
  Retrieves the next buffer from a queue, but doesn’t remove it.
- [func CMBufferQueueContainsEndOfData(CMBufferQueue) -> Bool](./cmbufferqueuecontainsendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](./cmbufferqueueisatendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegetbuffercount(_:))*