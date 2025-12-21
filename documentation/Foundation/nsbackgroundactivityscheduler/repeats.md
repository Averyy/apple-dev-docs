# repeats

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the activity should be rescheduled after it completes.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var repeats: Bool { get set }
```

#### Discussion

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false). See [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md).

## See Also

- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var interval: TimeInterval](nsbackgroundactivityscheduler/interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var qualityOfService: QualityOfService](nsbackgroundactivityscheduler/qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var shouldDefer: Bool](nsbackgroundactivityscheduler/shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](nsbackgroundactivityscheduler/tolerance.md)
  A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/repeats)*