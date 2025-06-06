# IODispatchQueue

**Framework**: DriverKit  
**Kind**: class

An object that manages the serial execution of blocks.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IODispatchQueue;
```

#### Overview

An [`IODispatchQueue`](iodispatchqueue.md) object is a FIFO queue that you use to execute tasks serially in your driver. You submit tasks as code blocks, and the system dequeues one block at a time, executing them sequentially.

> ❗ **Important**:  Always use an [`IODispatchQueue`](iodispatchqueue.md) instead of a [`dispatch_queue_t`](https://developer.apple.com/documentation/Dispatch/dispatch_queue_t) structure to schedule tasks for your driver.

 Always use an [`IODispatchQueue`](iodispatchqueue.md) instead of a [`dispatch_queue_t`](https://developer.apple.com/documentation/Dispatch/dispatch_queue_t) structure to schedule tasks for your driver.

## Topics

### Creating a Dispatch Queue
- [Create](iodispatchqueue/create.md)
  Creates a new dispatch queue object.
- [init](iodispatchqueue/init.md)
  Initializes the dispatch queue object.
- [free](iodispatchqueue/free.md)
  Performs any final cleanup for the dispatch queue object.
### Executing a Task Asynchronously
- [DispatchAsync](iodispatchqueue/dispatchasync.md)
  Schedule a block for asynchronous execution on the current queue.
- [DispatchAsync_f](iodispatchqueue/dispatchasync_f.md)
  Schedule a C-style function for asynchrous execution on the current queue.
- [IODispatchBlock](iodispatchblock.md)
  A block to execute on a dispatch queue.
- [IODispatchFunction](iodispatchfunction.md)
  A C-style function to execute on a dispatch queue.
### Executing a Task Synchronously
- [DispatchSync](iodispatchqueue/dispatchsync.md)
  Schedule a block for synchronous execution on the current queue.
- [DispatchSync_f](iodispatchqueue/dispatchsync_f.md)
  Schedule a C-style function for synchronous execution on the current queue.
### Stopping the Queue
- [Cancel](iodispatchqueue/cancel.md)
  Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.
- [IODispatchQueueCancelHandler](iodispatchqueuecancelhandler.md)
  A block to execute when a canceled dispatch queue stops executing tasks.
### Getting Queue Information
- [GetName](iodispatchqueue/getname.md)
  Returns the name of the queue as a C string.
- [OnQueue](iodispatchqueue/onqueue.md)
  Returns a Boolean value that indicates whether the current thread matches the dispatch queue’s thread.
- [IODispatchQueueName](iodispatchqueuename.md)
  A buffer for specifying the name of a dispatch queue.
### Logging Dispatch Information
- [Log](iodispatchqueue/log.md)
  Log the current execution context with respect to any queues the current thread holds.
- [IODispatchLogFunction](iodispatchlogfunction.md)
  A function that logs content.
### Instance Methods
- [DispatchConcurrent](iodispatchqueue/dispatchconcurrent.md)
- [DispatchConcurrent_f](iodispatchqueue/dispatchconcurrent_f.md)
- [RunAction](iodispatchqueue/runaction.md)
- [Sleep](iodispatchqueue/sleep.md)
- [SleepWithDeadline](iodispatchqueue/sleepwithdeadline.md)
- [SleepWithTimeout](iodispatchqueue/sleepwithtimeout.md)
- [Wakeup](iodispatchqueue/wakeup.md)
- [WakeupWithOptions](iodispatchqueue/wakeupwithoptions.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
  A dispatch source that reports hardware-related interrupt events to your driver.
- [IOTimerDispatchSource](iotimerdispatchsource.md)
  A dispatch source that notifies your driver at a specific time.
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
  A dispatch source that manages a shared-memory data queue.
- [IODispatchSource](iodispatchsource.md)
  The common base class for dispatch sources.
- [OSAction](osaction.md)
  An object that executes your driver’s custom behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue)*