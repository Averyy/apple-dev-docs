# CMBufferQueueContainsEndOfData(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set.

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
func CMBufferQueueContainsEndOfData(_ queue: CMBufferQueue) -> Bool
```

```c
extern Boolean CMBufferQueueContainsEndOfData(CMBufferQueueRef queue);
```

## Return Value

A Boolean indicating whether `CMBufferQueue` has been marked with `EndOfData`.

## Parameters

- `queue`: CMBufferQueue being interrogated.

## See Also

### Inspecting a Queue
- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](./cmbufferqueueisempty%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
- [func CMBufferQueueGetBufferCount(CMBufferQueue) -> CMItemCount](./cmbufferqueuegetbuffercount%28_%29.md)
  Gets the number of buffers in the queue.
- [func CMBufferQueueGetTotalSize(CMBufferQueue) -> Int](./cmbufferqueuegettotalsize%28_%29.md)
  Gets the total size of all sample buffers of a buffer queue.
- [func CMBufferQueueGetHead(CMBufferQueue) -> CMBuffer?](./cmbufferqueuegethead%28_%29.md)
  Retrieves the next buffer from a queue, but doesn’t remove it.
- [func CMBufferQueueIsAtEndOfData(CMBufferQueue) -> Bool](./cmbufferqueueisatendofdata%28_%29.md)
  Returns a Boolean value that indicates whether a buffer queue has its end-of-data marker set, and is now empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuecontainsendofdata(_:))*