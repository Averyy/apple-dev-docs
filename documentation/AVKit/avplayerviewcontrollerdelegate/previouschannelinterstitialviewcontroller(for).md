# previousChannelInterstitialViewController(for:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func previousChannelInterstitialViewController(for playerViewController: AVPlayerViewController) -> UIViewController
```

```objc
- (UIViewController *) previousChannelInterstitialViewControllerForPlayerViewController:(AVPlayerViewController *) playerViewController;
```

## Discussion

The framework calls this method when the user initiates, but hasn’t yet committed, a change in channel. The framework may call this method while a previous channel’s interstitial view is visible (on screen, or transitioning).

> ❗ **Important**:  Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Responding to channel changes
- [func playerViewController(AVPlayerViewController, skipToNextChannel: (Bool) -> Void)](./playerviewcontroller%28_,skiptonextchannel%29.md)
  Tells the delegate when the user wants to skip to the next channel.
- [func playerViewController(AVPlayerViewController, skipToPreviousChannel: (Bool) -> Void)](./playerviewcontroller%28_,skiptopreviouschannel%29.md)
  Tells the delegate when the user wants to skip to the previous channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./nextchannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for:))*