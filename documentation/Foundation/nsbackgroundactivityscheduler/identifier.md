# identifier

**Framework**: Foundation  
**Kind**: property

A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

This string should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. `nil` and zero-length strings are not allowed. See [`Configure Scheduler Properties`](nsbackgroundactivityscheduler#Configure-Scheduler-Properties.md).

## See Also

- [init(identifier: String)](nsbackgroundactivityscheduler/init(identifier:).md)
  Initializes a background activity scheduler object with a specified unique identifier.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/identifier)*