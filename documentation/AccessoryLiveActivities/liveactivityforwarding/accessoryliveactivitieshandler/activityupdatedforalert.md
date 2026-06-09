# activityUpdatedForAlert(_:)

**Framework**: Accessory Live Activities  
**Kind**: method  
**Required**: Yes

Provides an updated Live Activity and requests confirmation that the accessory displayed an alert.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
func activityUpdatedForAlert(_ activity: AccessoryLiveActivity) -> Bool
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Return Value

`true` if the accessory successfully displayed an alert for this update, `false` otherwise.

#### Overview

Use this callback method to keep the accessory’s display in sync with the current state of the Live Activity, display an included alert, and coordinate alerts across devices. Parse the activity’s details, select the information to display on your accessory, and convert it to data for transmission. Then, send the data to your accessory using the Live Activity’s corresponding [`LiveActivityForwarding.Session`](liveactivityforwarding/session.md) and its [`send(message:)`](liveactivityforwarding/session/send(message:).md) method.

If the activity’s [`state`](accessoryliveactivity/state.md) property equals [`ActivityState.dismissed`](https://developer.apple.com/documentation/ActivityKit/ActivityState/dismissed), remove the Live Activity from the accessory’s display.

> ❗ **Important**: The system uses the return value to coordinate alert behavior across devices and may suppress an alert on a paired iPhone. Make sure your return value is accurate to avoid someone missing an important Live Activity update.

## Parameters

- `activity`: An updated Live Activity that includes alert content.

## See Also

- [func activityUpdated(AccessoryLiveActivity)](liveactivityforwarding/accessoryliveactivitieshandler/activityupdated(_:).md)
  Provides an updated Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:))*