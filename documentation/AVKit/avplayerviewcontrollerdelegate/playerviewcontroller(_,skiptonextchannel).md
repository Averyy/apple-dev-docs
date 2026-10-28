# playerViewController(_:skipToNextChannel:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user wants to skip to the next channel.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, skipToNextChannel completion: @escaping @Sendable (Bool) -> Void)
```

```swift
optional func playerViewControllerSkipToNextChannel(_ playerViewController: AVPlayerViewController) async -> Bool
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController skipToNextChannel:(void (^)(BOOL success)) completion;
```

## Discussion

To enable channel skipping, adopt this method and replace the current player item with one that reflects the next channel’s content, and call the completion handler to dismiss the channel’s interstitial view. Each call to this method should advance one channel, relative to the previous request, even if the prior request hasn’t yet completed.

> ❗ **Important**:  Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## Parameters

- `playerViewController`: The player view controller.
- `completion`: A completion callback to invoke to dismiss the channel’s interstitial view.

## See Also

### Responding to channel changes
- [func playerViewController(AVPlayerViewController, skipToPreviousChannel: (Bool) -> Void)](./playerviewcontroller%28_,skiptopreviouschannel%29.md)
  Tells the delegate when the user wants to skip to the previous channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./nextchannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [func previousChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./previouschannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptonextchannel:))*