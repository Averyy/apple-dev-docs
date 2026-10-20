# translatesPlayerInterstitialEvents

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var translatesPlayerInterstitialEvents: Bool { get set }
```

```objc
@property (nonatomic) BOOL translatesPlayerInterstitialEvents;
```

#### Discussion

Enable this property value to support using interstitial events, or set it to [`false`](../../Swift/false.md) to perform your own interstitial management.

## See Also

### Configuring interstitial events
- [var integratedTimeline: AVPlayerItemIntegratedTimeline](./integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var automaticallyHandlesInterstitialEvents: Bool](./automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var interstitialTimeRanges: [AVInterstitialTimeRange]](./interstitialtimeranges.md)
  An array of time ranges that identify interstitial content.
- [var template: AVPlayerItem?](./template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/translatesplayerinterstitialevents)*