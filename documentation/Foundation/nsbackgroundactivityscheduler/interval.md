# interval

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An integer providing a suggested interval between scheduling and invoking the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var interval: TimeInterval { get set }
```

```objc
@property NSTimeInterval interval;
```

## Discussion

For repeating activities, the value of this property is also the suggested interval between invocations. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Background Scheduler Attributes
- [var identifier: String](./identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](./repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var shouldDefer: Bool](./shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](./tolerance.md)
  A value of type [`TimeInterval`](../timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/interval)*