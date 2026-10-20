# events

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current schedule of interstitial events.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var events: [AVPlayerInterstitialEvent]! { get set }
```

```objc
@property (copy, null_resettable) NSArray<AVPlayerInterstitialEvent *> * events;
```

#### Discussion

Setting this property to a non-`nil` value cancels and overrides all previously scheduled future interstitial events, including those that the primary item’s content specifies, such as directives carried by an HLS media playlists. Setting the value to an empty array clears the schedule or, if the server specifies interstitial events, reverts it to the server’s schedule.

> **Note**:  An event controller copies the events that you set for this value. Making subsequent changes to the events doesn’t impact the event schedule.

Changing the value of this property doesn’t impact currently playing interstitials. To cancel the current event, call [`cancelCurrentEvent(withResumptionOffset:)`](./cancelcurrentevent%28withresumptionoffset%29.md).

> ❗ **Important**:  The system raises an exception if you schedule an event that doesn’t provide the required data, such as one lacking a valid [`primaryItem`](../avplayerinterstitialevent/primaryitem.md) value, or a valid [`date`](../avplayerinterstitialevent/date.md) or [`time`](../avplayerinterstitialevent/time.md).

If you schedule interstitial events with dates that coincide either with the date of another scheduled interstitial event, or with a date range in the primary content’s timeline that the resumption offset of another scheduled interstitial event omits, the primary content remains suspended until all coinciding interstitial events complete. The system orders their playback according to their position in the array. The effective resumption offset is the sum of the resumption offsets of the coinciding events.

> **Note**:  Summing a numeric [`CMTime`](../../CoreMedia/cmtime.md) and an [`indefinite`](../../CoreMedia/cmtime/indefinite.md) time results in an [`indefinite`](../../CoreMedia/cmtime/indefinite.md) value.

## See Also

### Configuring the event schedule
- [func cancelCurrentEvent(withResumptionOffset: CMTime)](./cancelcurrentevent%28withresumptionoffset%29.md)
  Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.
- [func skipCurrentEvent()](./skipcurrentevent%28%29.md)
  Causes the playback of the currently playing interstital event to be abandoned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/events)*