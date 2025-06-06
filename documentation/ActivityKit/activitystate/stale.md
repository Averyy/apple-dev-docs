# ActivityState.stale

**Framework**: ActivityKit  
**Kind**: case

The Live Activity content is out of date and needs an update.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
case stale
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)

#### Discussion

The content of a Live Activity may become out of date before you can update it. For example, a person may be in an area without a network connection, causing the Live Activity to not receive updates. To tell people that they are looking at outdated Live Activity content, you can configure a [`staleDate`](activitycontent/staledate.md) for your Live Activity. At the specified date, the [`activityState`](activity/activitystate.md) changes to `stale` and you can update the Live Activity to indicate that its content is out of date.

## See Also

- [ActivityState.active](activitystate/active.md)
  The Live Activity is active, visible, and can receive content updates.
- [ActivityState.dismissed](activitystate/dismissed.md)
  The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.ended](activitystate/ended.md)
  The Live Activity is visible, but a person, app, or system ended it, and it won’t update its content anymore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitystate/stale)*