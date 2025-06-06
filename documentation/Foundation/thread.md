# Thread

**Framework**: Foundation  
**Kind**: class

A thread of execution.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class Thread
```

#### Overview

Use this class when you want to have an Objective-C method run in its own thread of execution. Threads are especially useful when you need to perform a lengthy task, but don’t want it to block the execution of the rest of the application. In particular, you can use threads to avoid blocking the main thread of the application, which handles user interface and event-related actions. Threads can also be used to divide a large job into several smaller jobs, which can lead to performance increases on multi-core computers.

The [`Thread`](thread.md) class supports semantics similar to those of [`Operation`](operation.md) for monitoring the runtime condition of a thread. You can use these semantics to cancel the execution of a thread or determine if the thread is still executing or has finished its task. Canceling a thread requires support from your thread code; see the description for [`cancel()`](thread/cancel().md) for more information.

##### Subclassing Notes

You can subclass [`Thread`](thread.md) and override the [`main()`](thread/main().md) method to implement your thread’s main entry point. If you override [`main()`](thread/main().md), you do not need to invoke the inherited behavior by calling `super`.

## Topics

### Initializing an NSThread Object
- [init()](thread/init.md)
  Returns an initialized `NSThread` object.
- [convenience init(target: Any, selector: Selector, object: Any?)](thread/init(target:selector:object:).md)
  Returns an `NSThread` object initialized with the given arguments.
### Starting a Thread
- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](thread/detachnewthreadselector(_:totarget:with:).md)
  Detaches a new thread and uses the specified selector as the thread entry point.
- [func start()](thread/start.md)
  Starts the receiver.
- [func main()](thread/main.md)
  The main entry point routine for the thread.
### Stopping a Thread
- [class func sleep(until: Date)](thread/sleep(until:).md)
  Blocks the current thread until the time specified.
- [class func sleep(forTimeInterval: TimeInterval)](thread/sleep(fortimeinterval:).md)
  Sleeps the thread for a given time interval.
- [class func exit()](thread/exit.md)
  Terminates the current thread.
- [func cancel()](thread/cancel.md)
  Changes the cancelled state of the receiver to indicate that it should exit.
### Determining the Thread’s Execution State
- [var isExecuting: Bool](thread/isexecuting.md)
  A Boolean value that indicates whether the receiver is executing.
- [var isFinished: Bool](thread/isfinished.md)
  A Boolean value that indicates whether the receiver has finished execution.
- [var isCancelled: Bool](thread/iscancelled.md)
  A Boolean value that indicates whether the receiver is cancelled.
### Working with the Main Thread
- [class var isMainThread: Bool](thread/ismainthread-swift.type.property.md)
  Returns a Boolean value that indicates whether the current thread is the main thread.
- [var isMainThread: Bool](thread/ismainthread-swift.property.md)
  A Boolean value that indicates whether the receiver is the main thread.
- [class var main: Thread](thread/main.md)
  Returns the `NSThread` object representing the main thread.
### Querying the Environment
- [class func isMultiThreaded() -> Bool](thread/ismultithreaded.md)
  Returns whether the application is multithreaded.
- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackReturnAddresses: [NSNumber]](thread/callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.
- [class var callStackSymbols: [String]](thread/callstacksymbols.md)
  Returns an array containing the call stack symbols.
### Working with Thread Properties
- [var threadDictionary: NSMutableDictionary](thread/threaddictionary.md)
  The thread object’s dictionary.
- [let NSAssertionHandlerKey: String](nsassertionhandlerkey.md)
  A key with a corresponding value in the thread dictionary.
- [var name: String?](thread/name.md)
  The name of the receiver.
- [var stackSize: Int](thread/stacksize.md)
  The stack size of the receiver, in bytes.
### Prioritizing Thread Work
- [var qualityOfService: QualityOfService](thread/qualityofservice.md)
- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.
- [class func threadPriority() -> Double](thread/threadpriority.md)
  Returns the current thread’s priority.
- [var threadPriority: Double](thread/threadpriority.md)
  The receiver’s priority
- [class func setThreadPriority(Double) -> Bool](thread/setthreadpriority(_:).md)
  Sets the current thread’s priority.
### Notifications
- [static let NSDidBecomeSingleThreaded: NSNotification.Name](nsnotification/name-swift.struct/nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSThreadWillExit: NSNotification.Name](nsnotification/name-swift.struct/nsthreadwillexit.md)
  An `NSThread` object posts this notification when it receives the [`exit()`](thread/exit().md) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits.
- [static let NSWillBecomeMultiThreaded: NSNotification.Name](nsnotification/name-swift.struct/nswillbecomemultithreaded.md)
  Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](thread/detachnewthreadselector(_:totarget:with:).md) or the [`start()`](thread/start().md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.
### Initializers
- [convenience init(block: () -> Void)](thread/init(block:).md)
### Type Methods
- [class func detachNewThread(() -> Void)](thread/detachnewthread(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSLocking](nslocking.md)
  The elementary methods adopted by classes that define lock objects.
- [class NSLock](nslock.md)
  An object that coordinates the operation of multiple threads of execution within the same application.
- [class NSRecursiveLock](nsrecursivelock.md)
  A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [class NSDistributedLock](nsdistributedlock.md)
  A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [class NSConditionLock](nsconditionlock.md)
  A lock that can be associated with specific, user-defined conditions.
- [class NSCondition](nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread)*