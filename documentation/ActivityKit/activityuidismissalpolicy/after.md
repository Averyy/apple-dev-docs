# after(_:)

**Framework**: ActivityKit  
**Kind**: method

The system removes the Live Activity that ended at the specified time within a four-hour window.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
static func after(_ date: Date) -> ActivityUIDismissalPolicy
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Discussion

Provide a date to tell the system when it should remove a Live Activity that ended. While you can provide any date, the system removes a Live Activity that ended after the specified date or after four hours from the moment the Live Activity ended — whichever comes first. When the system removes the Live Activity,  the [`ActivityState`](activitystate.md) changes to [`ActivityState.dismissed`](activitystate/dismissed.md).

## Parameters

- `date`: A date within a four-hour window from the moment the Live Activity ends.

## See Also

- [static let `default`: ActivityUIDismissalPolicy](activityuidismissalpolicy/default.md)
  The system’s default dismissal policy for the Live Activity.
- [static let immediate: ActivityUIDismissalPolicy](activityuidismissalpolicy/immediate.md)
  The system immediately removes the Live Activity that ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy/after(_:))*