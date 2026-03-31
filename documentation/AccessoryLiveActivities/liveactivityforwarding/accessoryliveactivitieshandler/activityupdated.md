# activityUpdated(_:)

**Framework**: Accessory Live Activities  
**Kind**: method  
**Required**: Yes

Provides an updated Live Activity.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func activityUpdated(_ activity: AccessoryLiveActivity)
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

#### Overview

Use this callback method to keep the accessory’s display in sync with the current state of the Live Activity. Parse the activity’s details, select the information to display on your accessory, and convert it to data for transmission. Then, send the data to your accessory using the Live Activity’s corresponding [`LiveActivityForwarding.Session`](liveactivityforwarding/session.md) and its [`send(message:)`](liveactivityforwarding/session/send(message:).md) method.

If the activity’s [`state`](accessoryliveactivity/state.md) property equals [`ActivityState.dismissed`](https://developer.apple.com/documentation/ActivityKit/ActivityState/dismissed), remove the Live Activity from the accessory’s display.

## Parameters

- `activity`: The updated Live Activity.

## See Also

- [func activityUpdatedForAlert(AccessoryLiveActivity) -> Bool](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md)
  Provides an updated Live Activity and requests confirmation that the accessory displayed an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler/activityupdated(_:))*