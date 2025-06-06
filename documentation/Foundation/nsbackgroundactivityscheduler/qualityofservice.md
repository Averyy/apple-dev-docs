# qualityOfService

**Framework**: Foundation  
**Kind**: property

A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var qualityOfService: QualityOfService { get set }
```

#### Discussion

Options include:

- NSQualityOfServiceUserInteractive
- NSQualityOfServiceUserInitiated
- NSQualityOfServiceUtility
- NSQualityOfServiceBackground

The default value is `NSQualityOfServiceBackground`. If you upgrade the quality of service above this level, the system schedules the activity more aggressively. The default value is the recommended value for most activities. See [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md). For information about quality of service, see [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](nsbackgroundactivityscheduler/repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](nsbackgroundactivityscheduler/interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var shouldDefer: Bool](nsbackgroundactivityscheduler/shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](nsbackgroundactivityscheduler/tolerance.md)
  A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/qualityofservice)*