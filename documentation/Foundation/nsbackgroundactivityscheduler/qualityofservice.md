# qualityOfService

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var qualityOfService: QualityOfService { get set }
```

```objc
@property NSQualityOfService qualityOfService;
```

#### Discussion

Options include:

- NSQualityOfServiceUserInteractive
- NSQualityOfServiceUserInitiated
- NSQualityOfServiceUtility
- NSQualityOfServiceBackground

The default value is `NSQualityOfServiceBackground`. If you upgrade the quality of service above this level, the system schedules the activity more aggressively. The default value is the recommended value for most activities. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties). For information about quality of service, see [Prioritize Work at the Task Level](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [Energy Efficiency Guide for Mac Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

### Background Scheduler Attributes
- [var identifier: String](./identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](./repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](./interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var shouldDefer: Bool](./shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](./tolerance.md)
  A value of type [`TimeInterval`](../timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/qualityofservice)*