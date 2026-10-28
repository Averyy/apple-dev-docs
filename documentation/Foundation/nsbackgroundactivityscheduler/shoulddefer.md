# shouldDefer

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var shouldDefer: Bool { get }
```

```objc
@property (readonly) BOOL shouldDefer;
```

## Discussion

Your app can check the `shouldDefer` property while executing scheduled background activity. If this property contains a value of [`true`](../../Swift/true.md), system conditions have changed since the time the activity started and deferral is recommended. For example, perhaps the user unplugged the Mac and it’s now running on battery power. In this case, your app should finish what it’s currently doing, save its state, and invoke its completion handler with a value of [`NSBackgroundActivityScheduler.Result.deferred`](./result/deferred.md). The system will invoke your activity again at a more optimal time, and your app can restore its previous state and resume where it left off. See [Detect Whether to Defer Activity](../nsbackgroundactivityscheduler.md#Detect-Whether-to-Defer-Activity) and [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Related Documentation
- [NSBackgroundActivityScheduler.Result](./result.md)
  These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.
### Background Scheduler Attributes
- [var identifier: String](./identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [var repeats: Bool](./repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](./interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var tolerance: TimeInterval](./tolerance.md)
  A value of type [`TimeInterval`](../timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/shoulddefer)*