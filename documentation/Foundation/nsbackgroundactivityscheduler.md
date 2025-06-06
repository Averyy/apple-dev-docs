# NSBackgroundActivityScheduler

**Framework**: Foundation  
**Kind**: class

A task scheduler suitable for low priority operations that can run in the background.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSBackgroundActivityScheduler
```

#### Overview

Use an [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md) object to schedule an arbitrary maintenance or background task. It’s similar to an [`Timer`](timer.md) object, in that it lets you schedule a repeating or non-repeating task. However, [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md) gives the system flexibility to determine the most efficient time to execute based on energy usage, thermal conditions, and CPU use.

For example, use an [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md) object to schedule:

- Automatic saves
- Backups
- Data maintenance
- Periodic content fetches
- Installation of updates
- Activities occurring in intervals of 10 minutes or more
- Any other deferrable task

For information about performing non-deferrable tasks efficiently, see [`Specify Nondeferrable Background Activities`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/SchedulingBackgroundActivity.html#//apple_ref/doc/uid/TP40013929-CH32-SW10) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

> **Note**:  The [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md) class interfaces with the XPC Activity API. However, your app doesn’t need to be an XPC service in order to use [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md).

##### Create a Scheduler

To initialize a scheduler, call [`init(identifier:)`](nsbackgroundactivityscheduler/init(identifier:).md) for `NSBackgroundActivityScheduler`, and pass it a unique identifier string in reverse DNS notation (`nil` and zero-length strings are not allowed) that remains constant across launches of your application.

> **Note**:  The system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future.

##### Configure Scheduler Properties

Configure the scheduler with any of the following scheduling properties:

- [`repeats`](nsbackgroundactivityscheduler/repeats.md)—If set to [`true`](https://developer.apple.com/documentation/swift/true), the activity is rescheduled at the specified interval after finishing.
- [`interval`](nsbackgroundactivityscheduler/interval.md)—For repeating schedulers, the average interval between invocations of the activity. For nonrepeating schedulers, `interval` is the suggested interval of time between scheduling the activity and the invocation of the activity.
- [`tolerance`](nsbackgroundactivityscheduler/tolerance.md)—The amount of time before or after the nominal fire date when the activity should be invoked. The nominal fire date is calculated by using the interval combined with the previous fire date or the time when the activity is started. These two properties create a window in time, during which the activity may be scheduled. The system will more aggressively schedule the activity as it nears the end of the grace period after the nominal fire date. The default value is half the interval.
- [`qualityOfService`](nsbackgroundactivityscheduler/qualityofservice.md)—The default value is `NSQualityOfServiceBackground`. If you upgrade the quality of service above this level, the system schedules the activity more aggressively. The default value is the recommended value for most activities. For information on quality of service, see [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

The next three code examples demonstrate different scheduling scenarios.

Scheduling an activity to fire in the next 10 minutes

Scheduling an activity to fire between 15 and 45 minutes from now

Scheduling an activity to fire once each hour

##### Schedule Activity with Schedulewithblock

When you’re ready to schedule the activity, call `scheduleWithBlock:` and provide a block of code to execute when the scheduler runs, as shown in the following example. The block will be called on a serial background queue appropriate for the level of quality of service specified. The system automatically uses the [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) method (of [`ProcessInfo`](processinfo.md)) while invoking the block, choosing appropriate options based on the specified quality of service.

When your block is called, it’s passed a completion handler as an argument. Configure the block to invoke this handler, passing it a result of type [`NSBackgroundActivityScheduler.Result`](nsbackgroundactivityscheduler/result.md) to indicate whether the activity finished ([`NSBackgroundActivityScheduler.Result.finished`](nsbackgroundactivityscheduler/result/finished.md)) or should be deferred ([`NSBackgroundActivityScheduler.Result.deferred`](nsbackgroundactivityscheduler/result/deferred.md)) and rescheduled for a later time. Failure to invoke the completion handler results in the activity not being rescheduled. For work that will be deferred and rescheduled, the block may optionally adjust scheduler properties, such as [`interval`](nsbackgroundactivityscheduler/interval.md) or [`tolerance`](nsbackgroundactivityscheduler/tolerance.md), before calling the completion handler.

Scheduling background activity

##### Detect Whether to Defer Activity

It’s conceivable that while a lengthy activity is running, conditions may change, resulting in the activity now requiring deferral. For example, perhaps the user has unplugged the Mac and it’s now running on battery power. Your activity can call [`shouldDefer`](nsbackgroundactivityscheduler/shoulddefer.md) to determine whether this has occurred. A value of [`true`](https://developer.apple.com/documentation/swift/true) indicates that the block should finish what it’s currently doing and invoke its completion handler with a value of [`NSBackgroundActivityScheduler.Result.deferred`](nsbackgroundactivityscheduler/result/deferred.md). See the following example.

Detecting deferred background activity

##### Stop Activity

Call [`invalidate()`](nsbackgroundactivityscheduler/invalidate().md) to stop scheduling an activity, as shown in the following example.

Stopping background activity

> **Note**:  When an activity is stopped, a block that’s currently executing will still finish executing.

## Topics

### Background Scheduler Attributes
- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](nsbackgroundactivityscheduler/repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](nsbackgroundactivityscheduler/interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var qualityOfService: QualityOfService](nsbackgroundactivityscheduler/qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var shouldDefer: Bool](nsbackgroundactivityscheduler/shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](nsbackgroundactivityscheduler/tolerance.md)
  A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.
### Initializing Schedulers
- [init(identifier: String)](nsbackgroundactivityscheduler/init(identifier:).md)
  Initializes a background activity scheduler object with a specified unique identifier.
### Scheduling Activity
- [func schedule((NSBackgroundActivityScheduler.CompletionHandler) -> Void)](nsbackgroundactivityscheduler/schedule(_:).md)
  Begins scheduling the background activity.
- [NSBackgroundActivityScheduler.CompletionHandler](nsbackgroundactivityscheduler/completionhandler.md)
### Stopping Scheduled Activity
- [func invalidate()](nsbackgroundactivityscheduler/invalidate.md)
  Prevents the background activity from being scheduled again.
### Constants
- [NSBackgroundActivityScheduler.Result](nsbackgroundactivityscheduler/result.md)
  These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.
- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.

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

- [class ProcessInfo](processinfo.md)
  A collection of information about the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/nsbackgroundactivityscheduler)*