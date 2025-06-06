# CMBufferQueueRemoveTrigger(_:triggerToken:)

**Framework**: Core Media  
**Kind**: func

Removes a previously installed trigger from a buffer queue.

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
func CMBufferQueueRemoveTrigger(_ queue: CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus
```

#### Return Value

A result code. See `Result Codes`

#### Discussion

Triggers will automatically be removed when a queue is finalized.  However, if more than one module has access to a queue, it may be hard for an individual module to know when the queue is finalized since other modules may retain it.  To address this concern, modules should remove their triggers before they themselves are finalized.

## Parameters

- `queue`:   from which the trigger is to be removed.
- `triggerToken`: Trigger to remove from the queue.

## See Also

- [func CMBufferQueueEnqueue(CMBufferQueue, buffer: CMBuffer) -> OSStatus](cmbufferqueueenqueue(_:buffer:).md)
  Enqueues a buffer onto a queue.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueueremovetrigger(_:triggertoken:))*