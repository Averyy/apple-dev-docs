# CMBufferQueue

**Framework**: Core Media

A queue of timed buffers.

#### Overview

Buffer queues are Core Foundation objects that implement a queue of timed buffers. The buffers can be of any Core Foundation-based type (`CFTypeRef`), but must have a concept of duration. When you create a buffer queue, you pass a set of callbacks, one of which is a required callback that returns the duration of the Core Foundation-based buffer object. The system invokes these callbacks synchronously on the thread that called the API.

Buffer queues support reading and writing data from different threads in a producer-consumer model. While this model typically has two threads (a producer and a consumer), a buffer queue can service any number of threads to enqueue and dequeue buffers. The system makes all operations atomic by use of a single mutex (one mutex per created queue object).

By default, a `CMBufferQueue` is a FIFO queue, but you can change that order by providing a comparison callback. For example, you might create a buffer queue where you enqueue buffers in decode order, and dequeue them in presentation order, by providing a comparison callback that sorts by presentation timestamp.

A buffer queue retains its enqueued buffers. When you call [`CMBufferQueueDequeue(_:)`](cmbufferqueuedequeue(_:).md), the system retains the buffer on behalf of the app, and the queue releases it. The retain count remains the same, but the app takes ownership of the buffer.

If you provide a buffer-readiness callback, an instance of `CMBufferQueue` can check for buffer readiness when calling the [`CMBufferQueueDequeueIfDataReady(_:)`](cmbufferqueuedequeueifdataready(_:).md) function. If you don’t provide that callback, the system assumes all buffers are ready, and there’s no difference between [`CMBufferQueueDequeue(_:)`](cmbufferqueuedequeue(_:).md) and [`CMBufferQueueDequeueIfDataReady(_:)`](cmbufferqueuedequeueifdataready(_:).md).

Buffer queues also provide the [`CMBufferQueueIsEmpty(_:)`](cmbufferqueueisempty(_:).md) and [`CMBufferQueueTestTrigger(_:triggerToken:)`](cmbufferqueuetesttrigger(_:triggertoken:).md) functions that, with the help of optional callbacks, get decode and presentation timestamps from a buffer. The system returns a value of [`invalid`](cmtime/invalid.md) if you don’t provide these callbacks.

You can set an end-of-data marker on a buffer queue, which causes further enqueues to fail. After the queue has dequeued all buffers, the queue is permanently empty (“at end of data”) until you call the [`CMBufferQueueReset(_:)`](cmbufferqueuereset(_:).md)function. Reset empties the queue and undoes the end-of-data marking.

You can interrogate the current status of a buffer queue. For example, you can test for emptiness ([`CMBufferQueueCreate(allocator:capacity:callbacks:queueOut:)`](cmbufferqueuecreate(allocator:capacity:callbacks:queueout:).md)), current queue duration (`Inspecting Buffer Queues`), and end-of-data status ([`CMBufferQueueContainsEndOfData(_:)`](cmbufferqueuecontainsendofdata(_:).md) and [`CMBufferQueueIsAtEndOfData(_:)`](cmbufferqueueisatendofdata(_:).md)).

You can install trigger callbacks by calling the [`CMBufferQueueInstallTriggerHandler(_:_:_:_:_:)`](cmbufferqueueinstalltriggerhandler(_:_:_:_:_:).md) function to get notifications of various queue state transitions, such as when the duration becomes less than a second. You can inspect a buffer queue during trigger callback, but you can’t modify it. You can test trigger conditions explicitly as well. You can invoke trigger callbacks from any buffer queue API that modifies the total duration of the queue, such as enqueuing, dequeuing, or resetting the queue. The system invokes trigger callbacks synchronously on the thread that called the API.

You can’t modify the state of the queue from within a trigger callback. The operation fails, returning a [`kCMBufferQueueError_CannotModifyQueueFromTriggerCallback`](kcmbufferqueueerror_cannotmodifyqueuefromtriggercallback.md) error. Attempting to enqueue a buffer when the queue is full, or dequeue from an empty queue, immediately returns an error (or a `NULL` buffer).

Install triggers to observe the queue’s fullness rather than repeatedly polling the queue to get this state.

## Topics

### Creating a Queue
- [func CMBufferQueueCreateWithHandlers(CFAllocator?, CMItemCount, OpaquePointer, UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](cmbufferqueuecreatewithhandlers(_:_:_:_:).md)
  Creates a buffer queue with handlers to inspect buffers.
- [func CMBufferQueueCreate(allocator: CFAllocator?, capacity: CMItemCount, callbacks: UnsafePointer<CMBufferCallbacks>, queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](cmbufferqueuecreate(allocator:capacity:callbacks:queueout:).md)
  Creates a buffer queue with callbacks to inspect buffers.
- [struct CMBufferCallbacks](cmbuffercallbacks.md)
  A structure that stores the callbacks that perform buffer operations.
### Managing a Queue
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
- [func CMBufferQueueRemoveTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> OSStatus](cmbufferqueueremovetrigger(_:triggertoken:).md)
  Removes a previously installed trigger from a buffer queue.
### Managing Triggers
- [func CMBufferQueueInstallTriggerHandler(CMBufferQueue, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandler(_:_:_:_:_:).md)
  Installs a trigger with a handler on a buffer queue.
- [func CMBufferQueueInstallTriggerHandlerWithIntegerThreshold(CMBufferQueue, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken?>?, CMBufferQueueTriggerHandler?) -> OSStatus](cmbufferqueueinstalltriggerhandlerwithintegerthreshold(_:_:_:_:_:).md)
  Installs a trigger with a handler and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerHandler](cmbufferqueuetriggerhandler.md)
  A type alias for a trigger handler.
- [typealias CMBufferQueueTriggerToken](cmbufferqueuetriggertoken.md)
  A type alias for a trigger token.
- [Buffer Trigger Conditions](buffer-trigger-conditions.md)
  The trigger conditions the framework supports.
- [func CMBufferQueueTestTrigger(CMBufferQueue, triggerToken: CMBufferQueueTriggerToken) -> Bool](cmbufferqueuetesttrigger(_:triggertoken:).md)
  Tests whether the trigger condition is true for the specified buffer queue.
- [func CMBufferQueueInstallTrigger(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, time: CMTime, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltrigger(_:callback:refcon:condition:time:triggertokenout:).md)
  Installs a trigger with a callback on a buffer queue.
- [func CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue, callback: CMBufferQueueTriggerCallback?, refcon: UnsafeMutableRawPointer?, condition: CMBufferQueueTriggerCondition, threshold: CMItemCount, triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken?>?) -> OSStatus](cmbufferqueueinstalltriggerwithintegerthreshold(_:callback:refcon:condition:threshold:triggertokenout:).md)
  Installs a trigger with a callback and threshold on a buffer queue.
- [typealias CMBufferQueueTriggerCallback](cmbufferqueuetriggercallback.md)
  A callback for the system to invoke when a trigger condition becomes true.
- [typealias CMBufferQueueTriggerCondition](cmbufferqueuetriggercondition.md)
  A type to specify conditions to associate with a buffer queue trigger.
### Inspecting Duration and Timing
- [func CMBufferQueueGetDuration(CMBufferQueue) -> CMTime](cmbufferqueuegetduration(_:).md)
  Gets the duration of a buffer queue.
- [func CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetmindecodetimestamp(_:).md)
  Gets the earliest decode timestamp of a buffer queue.
- [func CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetfirstdecodetimestamp(_:).md)
  Gets the decode timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetminpresentationtimestamp(_:).md)
  Gets the earliest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetfirstpresentationtimestamp(_:).md)
  Gets the presentation timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetendpresentationtimestamp(_:).md)
  Gets the greatest end presentation timestamp of a buffer queue.
- [func CMBufferQueueGetMaxPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetmaxpresentationtimestamp(_:).md)
  Gets the greatest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>](cmbufferqueuegetcallbacksforsamplebufferssortedbyoutputpts().md)
  Returns a pointer to a structure that contains callbacks to sort sample buffers by output presentation timestamp.
- [func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>](cmbufferqueuegetcallbacksforunsortedsamplebuffers().md)
  Returns a pointer to a callback structure for unsorted sample buffers.
### Inspecting a Queue
- [func CMBufferQueueIsEmpty(CMBufferQueue) -> Bool](cmbufferqueueisempty(_:).md)
  Returns a Boolean value that indicates whether a buffer queue is empty.
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
### Validating a Queue
- [func CMBufferQueueSetValidationHandler(CMBufferQueue, CMBufferValidationHandler) -> OSStatus](cmbufferqueuesetvalidationhandler(_:_:).md)
  A validation handler for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationHandler](cmbuffervalidationhandler.md)
  A type alias for a handler that tests whether a buffer is in a valid state to add to a queue.
- [func CMBufferQueueSetValidationCallback(CMBufferQueue, callback: CMBufferValidationCallback, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuesetvalidationcallback(_:callback:refcon:).md)
  A validation callback for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationCallback](cmbuffervalidationcallback.md)
  A type alias for a callback that tests whether a buffer is in a valid state to add to a queue.
### Accessing the Type Identifier
- [func CMBufferQueueGetTypeID() -> CFTypeID](cmbufferqueuegettypeid().md)
  Returns the type identifier of buffer queue objects.
### Data Types
- [class CMBufferQueue](cmbufferqueue.md)
  A reference to a buffer queue instance.
### Error Codes
- [Buffer Queue Error Codes](buffer-queue-errors.md)
  Error codes that framework operations produce.

## See Also

- [CMSimpleQueue](cmsimplequeue-api.md)
  A simple, lockless FIFO queue of elements.
- [CMMemoryPool](cmmemorypool-api.md)
  An object that optimizes memory allocation when working with large blocks of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue-api)*