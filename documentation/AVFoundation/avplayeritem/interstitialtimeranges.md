# interstitialTimeRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of time ranges that identify interstitial content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var interstitialTimeRanges: [AVInterstitialTimeRange] { get }
```

*tvOS*

```swift
var interstitialTimeRanges: [AVInterstitialTimeRange] { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, readonly) NSArray<AVInterstitialTimeRange *> * interstitialTimeRanges;
```

*tvOS*

```objc
@property (nonatomic, copy) NSArray<AVInterstitialTimeRange *> * interstitialTimeRanges;
```

## Discussion

Interstitial content is material that’s unrelated to a player item’s primary content, such as advertisements and legal notices. If you use [`AVPlayerViewController`](../../AVKit/avplayerviewcontroller.md) to present an item that contains interstitial time ranges, the user interface marks those time ranges differently on the playback timeline. A player view controller can also call your app when it begins and ends playing interstitial content. You can use these events to customize playback behavior, such as preventing viewers from skipping required content.

> **Note**:  On iOS, the stream must define the interstitial time ranges, or you must use [`AVPlayerInterstitialEventController`](../avplayerinterstitialeventcontroller.md).

## See Also

### Configuring interstitial events
- [var integratedTimeline: AVPlayerItemIntegratedTimeline](./integratedtimeline.md)
  An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [var automaticallyHandlesInterstitialEvents: Bool](./automaticallyhandlesinterstitialevents.md)
  A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [var translatesPlayerInterstitialEvents: Bool](./translatesplayerinterstitialevents.md)
  A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [var template: AVPlayerItem?](./template.md)
  The template player item that initializes this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/interstitialtimeranges)*