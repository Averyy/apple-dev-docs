# playerViewController(_:didPresent:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the player view controller finishes playing a range of interstitial content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didPresent interstitial: AVInterstitialTimeRange)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController didPresentInterstitialTimeRange:(AVInterstitialTimeRange *) interstitial;
```

## Discussion

Interstitial content is material that’s unrelated to the main content and may have special playback options or requirements. For example, implement this method to record when a user begins viewing an advertisement, or to enable the player view controller’s [`requiresLinearPlayback`](../avplayerviewcontroller/requireslinearplayback.md) property to prevent skipping mandatory legal notices.

Use the [`interstitialTimeRanges`](../../AVFoundation/avplayeritem/interstitialtimeranges.md) property to identify the time ranges of interstitial content in the media timeline.

## Parameters

- `playerViewController`: The player view controller.
- `interstitial`: The time range of interstitial content that’s finished playback.

## See Also

### Responding to interstitial content playback events
- [func playerViewController(AVPlayerViewController, willPresent: AVInterstitialTimeRange)](./playerviewcontroller%28_,willpresent%29.md)
  Tells the delegate when the player view controller is about to start playing a range of interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didpresent:))*