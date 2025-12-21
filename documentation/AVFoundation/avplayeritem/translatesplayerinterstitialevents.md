# translatesPlayerInterstitialEvents

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
@MainActor
var translatesPlayerInterstitialEvents: Bool { get set }
```

#### Discussion

Enable this property value to support using interstitial events, or set it to [`false`](https://developer.apple.com/documentation/Swift/false) to perform your own interstitial management.

## See Also

- [var integratedTimeline: AVPlayerItemIntegratedTimeline](avplayeritem/integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var automaticallyHandlesInterstitialEvents: Bool](avplayeritem/automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var interstitialTimeRanges: [AVInterstitialTimeRange]](avplayeritem/interstitialtimeranges.md)
  An array of time ranges that identify interstitial content.
- [var template: AVPlayerItem?](avplayeritem/template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/translatesplayerinterstitialevents)*