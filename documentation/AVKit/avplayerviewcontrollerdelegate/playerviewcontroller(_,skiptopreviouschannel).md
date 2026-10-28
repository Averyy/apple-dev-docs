# playerViewController(_:skipToPreviousChannel:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user wants to skip to the previous channel.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, skipToPreviousChannel completion: @escaping @Sendable (Bool) -> Void)
```

```swift
optional func playerViewControllerSkipToPreviousChannel(_ playerViewController: AVPlayerViewController) async -> Bool
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController skipToPreviousChannel:(void (^)(BOOL success)) completion;
```

## Discussion

Each call to this method should advance one channel, relative to the previous request, even if the prior request hasn’t yet completed. Adopt this method and replace the current player item with one that reflects the previous channel’s content, and call the completion block to dismiss the channel’s interstitial view.

> ❗ **Important**:  Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## Parameters

- `playerViewController`: The player view controller.
- `completion`: A completion callback to invoke to dismiss the channel’s interstitial view.

## See Also

### Responding to channel changes
- [func playerViewController(AVPlayerViewController, skipToNextChannel: (Bool) -> Void)](./playerviewcontroller%28_,skiptonextchannel%29.md)
  Tells the delegate when the user wants to skip to the next channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./nextchannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [func previousChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./previouschannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptopreviouschannel:))*