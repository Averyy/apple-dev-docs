# interval

**Framework**: Foundation  
**Kind**: property

An integer providing a suggested interval between scheduling and invoking the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var interval: TimeInterval { get set }
```

#### Discussion

For repeating activities, the value of this property is also the suggested interval between invocations. See [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md).

## See Also

- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](nsbackgroundactivityscheduler/repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var qualityOfService: QualityOfService](nsbackgroundactivityscheduler/qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var shouldDefer: Bool](nsbackgroundactivityscheduler/shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](nsbackgroundactivityscheduler/tolerance.md)
  A value of type [`TimeInterval`](timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/interval)*