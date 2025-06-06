# tolerance

**Framework**: Foundation  
**Kind**: property

A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var tolerance: TimeInterval { get set }
```

#### Discussion

A nominal fire date for scheduled background activity is calculated based on a combination of the [`interval`](nsbackgroundactivityscheduler/interval.md) property value and the time the activity began or the last execution date. The [`tolerance`](nsbackgroundactivityscheduler/tolerance.md) property specifies a grace period—a range of time before and after the nominal fire date, during which the activity may be invoked. As the activity nears the end of its grace period, the system schedules the activity more aggressively. The default tolerance period is half the value of the [`interval`](nsbackgroundactivityscheduler/interval.md) property. See [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md).

## See Also

- [typealias TimeInterval](timeinterval.md)
  A number of seconds.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/tolerance)*