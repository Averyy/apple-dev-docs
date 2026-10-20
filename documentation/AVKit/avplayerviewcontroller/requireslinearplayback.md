# requiresLinearPlayback

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the player allows someone to skip media content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var requiresLinearPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresLinearPlayback;
```

## Mentions

- [Adopting Picture in Picture in a standard player](../adopting-picture-in-picture-in-a-standard-player.md)
- [Working with interstitial content](../working-with-interstitial-content.md)

#### Discussion

If this value is `false` (the default), the controller’s user interface allows a user to fast-forward, scrub, or skip ahead to content later in the player’s presentation. To prevent the user from skipping content—for example, while presenting a legal notice or other mandatory interstitial content—set this property’s value to `true`.

To track when the player is presenting content for which you might require linear playback, use the [`interstitialTimeRanges`](../../AVFoundation/avplayeritem/interstitialtimeranges.md) property of the view controller’s player item to define the time ranges of the interstitial content. The view controller then sends [`playerViewController(_:willPresent:)`](../avplayerviewcontrollerdelegate/playerviewcontroller%28_,willpresent%29.md) and [`playerViewController(_:didPresent:)`](../avplayerviewcontrollerdelegate/playerviewcontroller%28_,didpresent%29.md) messages to its [`delegate`](./delegate.md) object when the content is playing. Implement these methods to enable or disable the [`requiresLinearPlayback`](./requireslinearplayback.md) property as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requireslinearplayback)*