# integratedTimeline

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An integrated timeline that represents the player item timing including its scheduled interstitial events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
var integratedTimeline: AVPlayerItemIntegratedTimeline { get }
```

```objc
@property (readonly) AVPlayerItemIntegratedTimeline * integratedTimeline;
```

#### Discussion

The value is `nil` for player items in an interstitial player.

## See Also

### Configuring interstitial events
- [var automaticallyHandlesInterstitialEvents: Bool](./automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var translatesPlayerInterstitialEvents: Bool](./translatesplayerinterstitialevents.md)
  A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [var interstitialTimeRanges: [AVInterstitialTimeRange]](./interstitialtimeranges.md)
  An array of time ranges that identify interstitial content.
- [var template: AVPlayerItem?](./template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/integratedtimeline)*