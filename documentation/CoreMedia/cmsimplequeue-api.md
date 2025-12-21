# CMSimpleQueue

**Framework**: Core Media

A simple, lockless FIFO queue of elements.

#### Overview

Simple queues are Core Foundation-based objects that implement a simple, lockless FIFO queue of (`void *`) elements. The elements in the queue can be pointers or simple pointer-sized numeric values (`NULL` or `0` elements aren’t allowed). If the elements are pointers to allocated memory buffers, handle lifetime management externally.

A simple queue can safely handle one enqueueing thread and one dequeueing thread. Simple queues are lockless, so enqueues and dequeues can occur on the Core Audio `ioProc` thread, where the system forbids locking and blocking.

You can query the state of a simple queue to get the current number of elements and the maximum capacity of the queue. You can also determine the queue’s fullness, which the system provides as a percentage of its capacity.

You can reset a simple queue, which returns it to its newly created state, with no elements in the queue (but with the maximum capacity unchanged).

## Topics

### Creating a Queue
- [func CMSimpleQueueCreate(allocator: CFAllocator?, capacity: Int32, queueOut: UnsafeMutablePointer<CMSimpleQueue?>) -> OSStatus](cmsimplequeuecreate(allocator:capacity:queueout:).md)
  Creates a queue that has the specified capacity.
### Managing Queues
- [func CMSimpleQueueEnqueue(CMSimpleQueue, element: UnsafeRawPointer) -> OSStatus](cmsimplequeueenqueue(_:element:).md)
  Enqueues an element in the queue.
- [func CMSimpleQueueDequeue(CMSimpleQueue) -> UnsafeRawPointer?](cmsimplequeuedequeue(_:).md)
  Dequeues an element from the queue.
- [func CMSimpleQueueReset(CMSimpleQueue) -> OSStatus](cmsimplequeuereset(_:).md)
  Resets the queue.
### Inspecting Queues
- [func CMSimpleQueueGetHead(CMSimpleQueue) -> UnsafeRawPointer?](cmsimplequeuegethead(_:).md)
  Returns the element at the head of the queue.
- [func CMSimpleQueueGetCapacity(CMSimpleQueue) -> Int32](cmsimplequeuegetcapacity(_:).md)
  Returns the number of elements that the queue can hold.
- [func CMSimpleQueueGetCount(CMSimpleQueue) -> Int32](cmsimplequeuegetcount(_:).md)
  Returns the number of elements currently in the queue.
### Accessing the Type Identifier
- [func CMSimpleQueueGetTypeID() -> CFTypeID](cmsimplequeuegettypeid().md)
  Returns the type identifier of sample buffer objects.
### Data Types
- [class CMSimpleQueue](cmsimplequeue.md)
  A reference to an instance that provides a simple lockless queue of elements.
### Errors
- [Simple Queue Error Codes](simple-queue-errors.md)
  Error codes that simple queue operations generate.

## See Also

- [CMBufferQueue](cmbufferqueue-api.md)
  A queue of timed buffers.
- [CMMemoryPool](cmmemorypool-api.md)
  An object that optimizes memory allocation when working with large blocks of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeue-api)*