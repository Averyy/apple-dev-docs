# ActivityUIDismissalPolicy

**Framework**: ActivityKit  
**Kind**: struct

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
- [static let `default`: ActivityUIDismissalPolicy](activityuidismissalpolicy/default.md)
  The system’s default dismissal policy for the Live Activity.
- [static let immediate: ActivityUIDismissalPolicy](activityuidismissalpolicy/immediate.md)
  The system immediately removes the Live Activity that ended.
- [static func after(Date) -> ActivityUIDismissalPolicy](activityuidismissalpolicy/after(_:).md)
  The system removes the Live Activity that ended at the specified time within a four-hour window.
### Operators
- [static func == (ActivityUIDismissalPolicy, ActivityUIDismissalPolicy) -> Bool](activityuidismissalpolicy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](activityuidismissalpolicy/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy) async](activity/end(_:dismissalpolicy:).md)
  Ends an active Live Activity.
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy, timestamp: Date) async](activity/end(_:dismissalpolicy:timestamp:).md)
  Ends an active Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy)*