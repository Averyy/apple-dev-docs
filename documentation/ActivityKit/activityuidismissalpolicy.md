# ActivityUIDismissalPolicy

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

The structure that describes when the system should remove a Live Activity that ended.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityUIDismissalPolicy
```

## Topics

### Dismissing a Live Activity
- [static let `default`: ActivityUIDismissalPolicy](./activityuidismissalpolicy/default.md)
  The system’s default dismissal policy for the Live Activity.
- [static let immediate: ActivityUIDismissalPolicy](./activityuidismissalpolicy/immediate.md)
  The system immediately removes the Live Activity that ended.
- [static func after(Date) -> ActivityUIDismissalPolicy](./activityuidismissalpolicy/after%28_%29.md)
  The system removes the Live Activity that ended at the specified time within a four-hour window.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Ending a Live Activity
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy) async](./activity/end%28_,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy, timestamp: Date) async](./activity/end%28_,dismissalpolicy,timestamp%29.md)
  Ends an active Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy)*