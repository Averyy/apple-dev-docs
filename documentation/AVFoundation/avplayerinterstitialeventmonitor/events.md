# events

**Framework**: AVFoundation  
**Kind**: property

The schedule of interstitial events.

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
var events: [AVPlayerInterstitialEvent] { get }
```

#### Discussion

When the primary player’s content specifies the schedule of interstitial events intrinsically, this property value typically changes whenever primary player’s [`currentItem`](avplayer/currentitem.md) changes. For HLS content that specifies interstitials using of `DATERANGE` tags, the value of this property may also change whenever the set of `DATERANGE` tags in the current item’s media playlist changes.

When you specify the schedule of interstitial events using an [`AVPlayerInterstitialEventController`](avplayerinterstitialeventcontroller.md), this property value changes only when you update the interstitial event controller’s schedule.

> **Note**:  The elements in the [`events`](avplayerinterstitialeventmonitor/events.md) array are immutable. Attempting to modify them generates an exception. To alter an event, make a copy and modify the new instance.

## See Also

- [class let eventsDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/eventsdidchangenotification.md)
  A notification the system posts when the monitor’s schedule of interstitial events changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/events)*