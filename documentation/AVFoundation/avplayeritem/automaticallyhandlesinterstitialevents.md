# automaticallyHandlesInterstitialEvents

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.

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
nonisolated
var automaticallyHandlesInterstitialEvents: Bool { get set }
```

## See Also

- [var integratedTimeline: AVPlayerItemIntegratedTimeline](avplayeritem/integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var translatesPlayerInterstitialEvents: Bool](avplayeritem/translatesplayerinterstitialevents.md)
  A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [var interstitialTimeRanges: [AVInterstitialTimeRange]](avplayeritem/interstitialtimeranges.md)
  An array of time ranges that identify interstitial content.
- [var template: AVPlayerItem?](avplayeritem/template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/automaticallyhandlesinterstitialevents)*