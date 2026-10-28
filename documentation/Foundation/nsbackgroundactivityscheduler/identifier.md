# identifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (copy, readonly) NSString * identifier;
```

## Discussion

This string should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. `nil` and zero-length strings are not allowed. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Related Documentation
- [init(identifier: String)](./init%28identifier%29.md)
  Initializes a background activity scheduler object with a specified unique identifier.
### Background Scheduler Attributes
- [var repeats: Bool](./repeats.md)
  A Boolean value indicating whether the activity should be rescheduled after it completes.
- [var interval: TimeInterval](./interval.md)
  An integer providing a suggested interval between scheduling and invoking the activity.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [var shouldDefer: Bool](./shoulddefer.md)
  A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [var tolerance: TimeInterval](./tolerance.md)
  A value of type [`TimeInterval`](../timeinterval.md), which specifies a range of time during which the background activity may occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/identifier)*