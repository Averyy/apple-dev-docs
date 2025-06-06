# Dispatch

**Framework**: Dispatch  
**Kind**: module

Execute code concurrently on multicore hardware by submitting work to dispatch queues managed by the system.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Dispatch, also known as Grand Central Dispatch (GCD), contains language features, runtime libraries, and system enhancements that provide systemic, comprehensive improvements to the support for concurrent code execution on multicore hardware in macOS, iOS, watchOS, and tvOS.

The BSD subsystem, Core Foundation, and Cocoa APIs have all been extended to use these enhancements to help both the system and your application to run faster, more efficiently, and with improved responsiveness. Consider how difficult it is for a single application to use multiple cores effectively, let alone to do it on different computers with different numbers of computing cores or in an environment with multiple applications competing for those cores. GCD, operating at the system level, can better accommodate the needs of all running applications, matching them to the available system resources in a balanced fashion.

##### Dispatch Objects and Arc

When you build your app using the Objective-C compiler, all dispatch objects are Objective-C objects. As such, when automatic reference counting (ARC) is enabled, dispatch objects are retained and released automatically, just like any other Objective-C object. When ARC is not enabled, use the [`dispatch_retain`](dispatch_retain.md) and [`dispatch_release`](dispatch_release.md) functions (or Objective-C semantics) to retain and release your dispatch objects. You cannot use the Core Foundation retain and release functions.

If you need to use retain and release semantics in an ARC-enabled app with a later deployment target (for maintaining compatibility with existing code), you can disable Objective-C-based dispatch objects by adding `-DOS_OBJECT_USE_OBJC=0` to your compiler flags.

## Topics

### Queues and Tasks
- [class DispatchQueue](dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchWorkItem](dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [class DispatchGroup](dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Queue](dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
### Thread Scheduling
- [struct DispatchQoS](dispatchqos.md)
  The quality of service, or the execution priority, to apply to tasks.
### System Event Monitoring
- [class DispatchSource](dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchData](dispatchdata.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [struct DispatchDataIterator](dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.
### Task Synchronization
- [class DispatchSemaphore](dispatchsemaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Semaphore](dispatch-semaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](dispatch-barrier.md)
  A synchronization point for tasks executing in a concurrent dispatch queue.
### Time Constructs
- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
- [enum DispatchTimeInterval](dispatchtimeinterval.md)
  A number of seconds, millisconds, microseconds, or nanoseconds.
- [enum DispatchTimeoutResult](dispatchtimeoutresult.md)
  A result value indicating whether a dispatch operation finished before a specified time.
- [typealias dispatch_time_t](dispatch_time_t.md)
  An abstract representation of time.
- [var DISPATCH_WALLTIME_NOW: UInt](dispatch_walltime_now.md)
  The current time.
- [Wall Time Constants](2963138-wall-time-constants.md)
  Constants for wall time values.
### Dispatch Objects
- [class DispatchObject](dispatchobject.md)
  The base class for most dispatch types.
- [enum DispatchPredicate](dispatchpredicate.md)
  Logical conditions to evaluate within a given execution context.
- [func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)](dispatchprecondition(condition:).md)
  Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](dispatch-objects.md)
  The basic behaviors supported by all dispatch types.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
### Classes
- [class DispatchWorkloop](dispatchworkloop.md)
### Reference
- [Dispatch Constants](dispatch-constants.md)
- [Dispatch Data Types](dispatch-data-types.md)
- [Dispatch Functions](dispatch-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Dispatch)*