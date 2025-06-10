# update(_:alertConfiguration:timestamp:)

**Framework**: ActivityKit  
**Kind**: method

Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
func update(_ content: ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration? = nil, timestamp: Date) async
```

#### Discussion

The system ignores updates to a Live Activity that’s in the [`ActivityState.ended`](activitystate/ended.md) state.

## Parameters

- `content`: The updated dynamic content for the Live Activity. The size of its    property can’t exceed 4KB in size.
- `alertConfiguration`: The alert configuration you use to configure how the system notifies   a person about the updated content of the Live Activity.
- `timestamp`: The time the data in the payload was generated. If this is older than a previous   update or push payload, the system ignores this update.

## See Also

- [func update(ActivityContent<Activity<Attributes>.ContentState>) async](activity/update(_:).md)
  Updates the dynamic content of the Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?) async](activity/update(_:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [struct AlertConfiguration](alertconfiguration.md)
  A structure you use to configure an alert that appears when you update your Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/update(_:alertconfiguration:timestamp:))*