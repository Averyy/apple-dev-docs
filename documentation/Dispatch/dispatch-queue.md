# Dispatch Queue

**Framework**: Dispatch  
**Role**: API Collection

An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.

## Overview

Dispatch queues are FIFO queues to which your application can submit tasks in the form of block objects. Dispatch queues execute tasks either serially or concurrently. Work submitted to dispatch queues executes on a pool of threads managed by the system. Except for the dispatch queue representing your app’s main thread, the system makes no guarantees about which thread it uses to execute a task.

You schedule work items synchronously or asynchronously. When you schedule a work item synchronously, your code waits until that item finishes execution. When you schedule a work item asynchronously, your code continues executing while the work item runs elsewhere.

> ❗ **Important**:  Attempting to synchronously execute a work item on the main queue results in deadlock.

Dispatch queues provide minimal support for autoreleased objects by default. System APIs may return autoreleased objects to your code. For example, [`NSError`](../Foundation/nserror.md) objects are often autoreleased. If you see memory pressure increase because of autoreleased objects created in your blocks, consider adding autorelease pools to those blocks to relieve the pressure. You can also configure the default autorelease behavior of any custom dispatch queues using the [`dispatch_queue_attr_make_with_autorelease_frequency`](./dispatch_queue_attr_make_with_autorelease_frequency.md) function at creation time.

### Avoiding Excessive Thread Creation

When designing tasks for concurrent execution, do not call methods that block the current thread of execution. When a task scheduled by a concurrent dispatch queue blocks a thread, the system creates additional threads to run other queued concurrent tasks. If too many tasks block, the system may run out of threads for your app.

Another way that apps consume too many threads is by creating too many private concurrent dispatch queues. Because each dispatch queue consumes thread resources, creating additional concurrent dispatch queues exacerbates the thread consumption problem. Instead of creating private concurrent queues, submit tasks to one of the global concurrent dispatch queues. For serial tasks, set the target of your serial queue to one of the global concurrent queues. That way, you can maintain the serialized behavior of the queue while minimizing the number of separate queues creating threads.

## Topics

### Creating a Dispatch Queue
- [typealias dispatch_queue_t](./dispatch_queue_t.md)
  A lightweight object to which your application submits blocks for subsequent execution.
- [typealias dispatch_queue_main_t](./dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](./dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](./dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](./dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create](./dispatch_queue_create.md)
  Creates a new dispatch queue to which you can submit blocks.
- [dispatch_queue_create_with_target](./dispatch_queue_create_with_target.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DISPATCH_QUEUE_SERIAL](./dispatch_queue_serial.md)
  A dispatch queue that executes blocks serially in FIFO order.
- [DISPATCH_QUEUE_CONCURRENT](./dispatch_queue_concurrent.md)
  A dispatch queue that executes blocks concurrently.
### Configuring Queue Execution Parameters
- [typealias dispatch_queue_attr_t](./dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_attr_make_with_qos_class](./dispatch_queue_attr_make_with_qos_class.md)
  Returns attributes suitable for creating a dispatch queue with the desired quality-of-service information.
- [dispatch_queue_get_qos_class](./dispatch_queue_get_qos_class.md)
  Returns the quality-of-service class for the specified queue.
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_attr_make_initially_inactive](./dispatch_queue_attr_make_initially_inactive.md)
  Returns an attribute that configures a dispatch queue as initially inactive.
- [dispatch_queue_attr_make_with_autorelease_frequency](./dispatch_queue_attr_make_with_autorelease_frequency.md)
  Returns an attribute that specifies how the dispatch queue manages autorelease pools for the blocks it executes.
- [dispatch_autorelease_frequency_t](./dispatch_autorelease_frequency_t.md)
  Constants indicating the frequency with which a dispatch queue creates autorelease pools for its tasks.
### Executing Tasks Synchronously
- [func sync(execute: () -> Void)](./dispatchqueue/sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func asyncAndWait(execute: () -> Void)](./dispatchqueue/asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.
- [dispatch_sync_f](./dispatch_sync_f.md)
  Submits an app-defined function for synchronous execution on a dispatch queue.
- [dispatch_async_and_wait_f](./dispatch_async_and_wait_f.md)
  Submits a function-based work item for execution and returns only after it finishes executing.
- [dispatch_barrier_async_and_wait](./dispatch_barrier_async_and_wait.md)
  Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](./dispatch_barrier_async_and_wait_f.md)
  Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
### Managing Queue Attributes
- [func setTarget(queue: dispatch_queue_t?)](./dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.
- [dispatch_queue_get_label](./dispatch_queue_get_label.md)
  Returns the label you assigned to the dispatch queue at creation time.
- [DISPATCH_CURRENT_QUEUE_LABEL](./dispatch_current_queue_label.md)
  Pass this constant to the [`dispatch_queue_get_label`](./dispatch_queue_get_label.md) function to retrieve the label of the current queue.
### Managing the Main Dispatch Queue
- [func dispatchMain() -> Never](./dispatchmain%28%29.md)
  Executes blocks submitted to the main queue.
### Executing Tasks Asynchronously
- [dispatch_async](./dispatch_async.md)
  Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_async_f](./dispatch_async_f.md)
  Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](./dispatch_after.md)
  Enqueues a block for execution at the specified time.
- [dispatch_after_f](./dispatch_after_f.md)
  Enqueues an app-defined function for execution at the specified time.
- [dispatch_function_t](./dispatch_function_t.md)
  The prototype of functions submitted to dispatch queues.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
### Executing a Task Only Once
- [dispatch_once](./dispatch_once-c.func.md)
  Executes a block object only once for the lifetime of an application.
- [dispatch_once_f](./dispatch_once_f-c.func.md)
  Executes an application-defined function only once for the lifetime of an application.
- [dispatch_once_t](./dispatch_once_t.md)
  A predicate for use with the `dispatch_once` function.
### Executing a Task in Parallel
- [dispatch_apply](./dispatch_apply.md)
  Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.
- [dispatch_apply_f](./dispatch_apply_f.md)
  Submits a single function to the dispatch queue and causes the function to be executed the specified number of times.
- [DISPATCH_APPLY_AUTO](./dispatch_apply_auto.md)
### Executing a Barrier Task
- [dispatch_barrier_async](./dispatch_barrier_async.md)
  Submits a barrier block for asynchronous execution and returns immediately.
- [dispatch_barrier_async_f](./dispatch_barrier_async_f.md)
  Submits a barrier function for asynchronous execution and returns immediately.
- [dispatch_barrier_sync](./dispatch_barrier_sync.md)
  Submits a barrier block object for execution and waits until that block completes.
- [dispatch_barrier_sync_f](./dispatch_barrier_sync_f.md)
  Submits a barrier function for execution and waits until that function completes.
### Getting and Setting Contextual Data
- [dispatch_get_specific](./dispatch_get_specific.md)
  Returns the value for the key associated with the current dispatch queue.
- [dispatch_queue_set_specific](./dispatch_queue_set_specific.md)
  Sets the key/value data for the specified dispatch queue.
- [dispatch_queue_get_specific](./dispatch_queue_get_specific.md)
  Gets the value for the key associated with the specified dispatch queue.
### Testing the Execution Context
- [dispatch_assert_queue](./dispatch_assert_queue.md)
  Generates an assertion if the current block is not running on the specified dispatch queue.
- [dispatch_assert_queue_barrier](./dispatch_assert_queue_barrier.md)
  Generates an assertion if the current block is not running as a barrier on the specified dispatch queue.
- [dispatch_assert_queue_not](./dispatch_assert_queue_not.md)
  Generates an assertion if the current block is executing on the specified dispatch queue.

## See Also

### Queues and Tasks
- [class DispatchQueue](./dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchWorkItem](./dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [class DispatchGroup](./dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Work Item](./dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](./dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](./workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-queue)*