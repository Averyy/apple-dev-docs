# immediate

**Framework**: ActivityKit  
**Kind**: property

The system immediately removes the Live Activity that ended.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
static let immediate: ActivityUIDismissalPolicy
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Discussion

With the `immediate` dismissal policy, the system immediately removes the ended Live Activity and the [`ActivityState`](activitystate.md) changes to [`ActivityState.dismissed`](activitystate/dismissed.md).

## See Also

- [static let `default`: ActivityUIDismissalPolicy](activityuidismissalpolicy/default.md)
  The system’s default dismissal policy for the Live Activity.
- [static func after(Date) -> ActivityUIDismissalPolicy](activityuidismissalpolicy/after(_:).md)
  The system removes the Live Activity that ended at the specified time within a four-hour window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/immediate)*