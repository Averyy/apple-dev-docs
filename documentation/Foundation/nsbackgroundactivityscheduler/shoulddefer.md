# shouldDefer

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var shouldDefer: Bool { get }
```

#### Discussion

Your app can check the `shouldDefer` property while executing scheduled background activity. If this property contains a value of [`true`](https://developer.apple.com/documentation/swift/true), system conditions have changed since the time the activity started and deferral is recommended. For example, perhaps the user unplugged the Mac and it’s now running on battery power. In this case, your app should finish what it’s currently doing, save its state, and invoke its completion handler with a value of [`NSBackgroundActivityScheduler.Result.deferred`](nsbackgroundactivityscheduler/result/deferred.md). The system will invoke your activity again at a more optimal time, and your app can restore its previous state and resume where it left off. See [`Detect Whether to Defer Activity`](nsbackgroundactivityscheduler#Detect-Whether-to-Defer-Activity.md) and [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md).

## See Also

- [NSBackgroundActivityScheduler.Result](nsbackgroundactivityscheduler/result.md)
  These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.
- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](nsbackgroundactivityscheduler/repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](nsbackgroundactivityscheduler/interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var qualityOfService: QualityOfService](nsbackgroundactivityscheduler/qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var tolerance: TimeInterval](nsbackgroundactivityscheduler/tolerance.md)
  A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/shoulddefer)*