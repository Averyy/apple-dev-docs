# update(using:)

**Framework**: Activitykit  
**Kind**: method

Updates the dynamic content of the Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
func update(using contentState: Activity<Attributes>.ContentState) async
```

#### Discussion

Use this function to update the Live Activity while your app is in the foreground or while it’s in the background — for example, by using [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

> **Note**: The system ignores attempts to update a Live Activity that ended.

## Parameters

- `contentState`: The updated dynamic content for the Live Activity. The size of   the encoded content can’t exceed 4KB in size.

## See Also

- [func update(ActivityContent<Activity<Attributes>.ContentState>) async](activity/update(_:).md)
  Updates the dynamic content of the Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?) async](activity/update(_:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [struct AlertConfiguration](alertconfiguration.md)
  A structure you use to configure an alert that appears when you update your Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?, timestamp: Date) async](activity/update(_:alertconfiguration:timestamp:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/update(using:))*