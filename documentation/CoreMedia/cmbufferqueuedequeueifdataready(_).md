# CMBufferQueueDequeueIfDataReady(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Dequeues a buffer from a queue, if it’s ready.

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
func CMBufferQueueDequeueIfDataReady(_ queue: CMBufferQueue) -> CMBuffer?
```

```c
extern CMBufferRefCMBufferQueueDequeueIfDataReadyAndRetain(CMBufferQueueRef queue);
```

## Return Value

The dequeued buffer.  Will be `NULL` if the queue is empty, or if the buffer to be dequeued is not yet ready.

## Discussion

The buffer is released by the queue, but it is also retained for the client. Buffer ownership is thereby transferred from queue to client.  The client need not retain the buffer, but is responsible to release it when done with it.

## Parameters

- `queue`: The `CMBufferQueue` from which to dequeue a buffer (if the buffer is ready).

## See Also

### Managing a Queue
- [func CMBufferQueueEnqueue(CMBufferQueue, buffer: CMBuffer) -> OSStatus](./cmbufferqueueenqueue%28_,buffer%29.md)
  Enqueues a buffer onto a queue.
- [func CMBufferQueueCallForEachBuffer(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, refcon: UnsafeMutableRawPointer?) -> OSStatus](./cmbufferqueuecallforeachbuffer%28_,callback,refcon%29.md)
  Calls a function for every buffer in a queue.
- [func CMBufferQueueDequeue(CMBufferQueue) -> CMBuffer?](./cmbufferqueuedequeue%28_%29.md)
  Dequeues a buffer from a queue.
- [func CMBufferQueueMarkEndOfData(CMBufferQueue) -> OSStatus](./cmbufferqueuemarkendofdata%28_%29.md)
  Sets a marker to indicate this queue doesn’t allow enqueuing new buffers.
- [func CMBufferQueueReset(CMBufferQueue) -> OSStatus](./cmbufferqueuereset%28_%29.md)
  Resets a buffer queue, which allows it to enqueue new buffers.
- [func CMBufferQueueResetWithCallback(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> Void, refcon: UnsafeMutableRawPointer?) -> OSStatus](./cmbufferqueueresetwithcallback%28_,callback,refcon%29.md)
  A callback that invokes a function for every buffer in a queue and then resets the queue.
- [func CMBufferQueueRemoveTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus](./cmbufferqueueremovetrigger%28_,triggertoken%29.md)
  Removes a previously installed trigger from a buffer queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuedequeueifdataready(_:))*