# CMBufferQueueEnqueue(_:buffer:)

**Framework**: Core Media  
**Kind**: func

Enqueues a buffer onto a queue.

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
func CMBufferQueueEnqueue(_ queue: CMBufferQueue, buffer buf: CMBuffer) -> OSStatus
```

#### Return Value

A result code. See `Result Codes`.

#### Discussion

The buffer is retained by the queue, so the client can safely release the buffer if it has no further use for it. If the compare callback is non-`NULL`, this API performs an insertion sort using that compare operation. If the validation callback is non-`NULL`, this API calls it; if it returns a nonzero `OSStatus`, the buffer will not be enqueued and this API will return the same error `OSStatus`.

## Parameters

- `queue`: The   on which to enqueue the buffer.
- `buf`: The buffer to enqueue.

## See Also

- [func CMBufferQueueCallForEachBuffer(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuecallforeachbuffer(_:callback:refcon:).md)
  Calls a function for every buffer in a queue.
- [func CMBufferQueueDequeue(CMBufferQueue) -> CMBuffer?](cmbufferqueuedequeue(_:).md)
  Dequeues a buffer from a queue.
- [func CMBufferQueueDequeueIfDataReady(CMBufferQueue) -> CMBuffer?](cmbufferqueuedequeueifdataready(_:).md)
  Dequeues a buffer from a queue, if it’s ready.
- [func CMBufferQueueMarkEndOfData(CMBufferQueue) -> OSStatus](cmbufferqueuemarkendofdata(_:).md)
  Sets a marker to indicate this queue doesn’t allow enqueuing new buffers.
- [func CMBufferQueueReset(CMBufferQueue) -> OSStatus](cmbufferqueuereset(_:).md)
  Resets a buffer queue, which allows it to enqueue new buffers.
- [func CMBufferQueueResetWithCallback(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> Void, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueueresetwithcallback(_:callback:refcon:).md)
  A callback that invokes a function for every buffer in a queue and then resets the queue.
- [func CMBufferQueueRemoveTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus](cmbufferqueueremovetrigger(_:triggertoken:).md)
  Removes a previously installed trigger from a buffer queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueueenqueue(_:buffer:))*