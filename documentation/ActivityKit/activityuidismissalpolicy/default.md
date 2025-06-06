# default

**Framework**: ActivityKit  
**Kind**: property

The system’s default dismissal policy for the Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
static let `default`: ActivityUIDismissalPolicy
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Discussion

With the default dismissal policy, the system keeps a Live Activity that ended on the Lock Screen for up to four hours after it ends or a person removes it. The [`ActivityState`](activitystate.md) doesn’t change to [`ActivityState.dismissed`](activitystate/dismissed.md) until a person or the system removes the Live Activity user interface.

## See Also

- [static let immediate: ActivityUIDismissalPolicy](activityuidismissalpolicy/immediate.md)
  The system immediately removes the Live Activity that ended.
- [static func after(Date) -> ActivityUIDismissalPolicy](activityuidismissalpolicy/after(_:).md)
  The system removes the Live Activity that ended at the specified time within a four-hour window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/default)*