# interstitialTimeRanges

**Framework**: Avfoundation  
**Kind**: property

An array of time ranges that identify interstitial content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var interstitialTimeRanges: [AVInterstitialTimeRange] { get set }
```

#### Discussion

Interstitial content is material that’s unrelated to a player item’s primary content, such as advertisements and legal notices. If you use [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) to present an item that contains interstitial time ranges, the user interface marks those time ranges differently on the playback timeline. A player view controller can also call your app when it begins and ends playing interstitial content. You can use these events to customize playback behavior, such as preventing viewers from skipping required content.

> **Note**:  On iOS, the stream must define the interstitial time ranges, or you must use [`AVPlayerInterstitialEventController`](avplayerinterstitialeventcontroller.md).

## See Also

- [var integratedTimeline: AVPlayerItemIntegratedTimeline](avplayeritem/integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var automaticallyHandlesInterstitialEvents: Bool](avplayeritem/automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var translatesPlayerInterstitialEvents: Bool](avplayeritem/translatesplayerinterstitialevents.md)
  A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [var template: AVPlayerItem?](avplayeritem/template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/interstitialtimeranges)*