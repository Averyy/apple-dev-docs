# CMBufferQueueMarkEndOfData(_:)

**Framework**: Core Media  
**Kind**: func

Sets a marker to indicate this queue doesn’t allow enqueuing new buffers.

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
func CMBufferQueueMarkEndOfData(_ queue: CMBufferQueue) -> OSStatus
```

#### Return Value

A result code. See `Result Codes`

#### Discussion

All subsequent Enqueues will be rejected until [`CMBufferQueueReset(_:)`](cmbufferqueuereset(_:).md) is called. Subsequent Dequeues will succeed as long as the queue is not empty.

## Parameters

- `queue`: The   being marked.

## See Also

- [func CMBufferQueueEnqueue(CMBufferQueue, buffer: CMBuffer) -> OSStatus](cmbufferqueueenqueue(_:buffer:).md)
  Enqueues a buffer onto a queue.
- [func CMBufferQueueCallForEachBuffer(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> OSStatus, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuecallforeachbuffer(_:callback:refcon:).md)
  Calls a function for every buffer in a queue.
- [func CMBufferQueueDequeue(CMBufferQueue) -> CMBuffer?](cmbufferqueuedequeue(_:).md)
  Dequeues a buffer from a queue.
- [func CMBufferQueueDequeueIfDataReady(CMBufferQueue) -> CMBuffer?](cmbufferqueuedequeueifdataready(_:).md)
  Dequeues a buffer from a queue, if it’s ready.
- [func CMBufferQueueReset(CMBufferQueue) -> OSStatus](cmbufferqueuereset(_:).md)
  Resets a buffer queue, which allows it to enqueue new buffers.
- [func CMBufferQueueResetWithCallback(CMBufferQueue, callback: (CMBuffer, UnsafeMutableRawPointer?) -> Void, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueueresetwithcallback(_:callback:refcon:).md)
  A callback that invokes a function for every buffer in a queue and then resets the queue.
- [func CMBufferQueueRemoveTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus](cmbufferqueueremovetrigger(_:triggertoken:).md)
  Removes a previously installed trigger from a buffer queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuemarkendofdata(_:))*