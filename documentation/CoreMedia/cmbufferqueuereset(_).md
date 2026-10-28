# CMBufferQueueReset(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Resets a buffer queue, which allows it to enqueue new buffers.

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
func CMBufferQueueReset(_ queue: CMBufferQueue) -> OSStatus
```

```c
extern OSStatus CMBufferQueueReset(CMBufferQueueRef queue);
```

## Return Value

A result code. See `Result Codes`.

## Discussion

All buffers in the queue are released.  Triggers are not removed, however, and will be called appropriately as the queue duration goes to zero.

## Parameters

- `queue`: The `CMBufferQueue` being reset.

## See Also

### Managing a Queue
- [func CMBufferQueueEnqueue(CMBufferQueue, buffer: CMBuffer) -> OSStatus](./cmbufferqueueenqueue%28_,buffer%29.md)
  Enqueues a buffer onto a queue.
- [func CMBufferQueueCallForEachBuffer(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, refcon: UnsafeMutableRawPointer?) -> OSStatus](./cmbufferqueuecallforeachbuffer%28_,callback,refcon%29.md)
  Calls a function for every buffer in a queue.
- [func CMBufferQueueDequeue(CMBufferQueue) -> CMBuffer?](./cmbufferqueuedequeue%28_%29.md)
  Dequeues a buffer from a queue.
- [func CMBufferQueueDequeueIfDataReady(CMBufferQueue) -> CMBuffer?](./cmbufferqueuedequeueifdataready%28_%29.md)
  Dequeues a buffer from a queue, if it’s ready.
- [func CMBufferQueueMarkEndOfData(CMBufferQueue) -> OSStatus](./cmbufferqueuemarkendofdata%28_%29.md)
  Sets a marker to indicate this queue doesn’t allow enqueuing new buffers.
- [func CMBufferQueueResetWithCallback(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> Void, refcon: UnsafeMutableRawPointer?) -> OSStatus](./cmbufferqueueresetwithcallback%28_,callback,refcon%29.md)
  A callback that invokes a function for every buffer in a queue and then resets the queue.
- [func CMBufferQueueRemoveTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus](./cmbufferqueueremovetrigger%28_,triggertoken%29.md)
  Removes a previously installed trigger from a buffer queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuereset(_:))*