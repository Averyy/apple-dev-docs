# playerViewController(_:skipToPreviousChannel:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the user wants to skip to the previous channel.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func playerViewControllerSkipToPreviousChannel(_ playerViewController: AVPlayerViewController) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func playerViewControllerSkipToPreviousChannel(_ playerViewController: AVPlayerViewController) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func playerViewControllerSkipToPreviousChannel(_ playerViewController: AVPlayerViewController) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Each call to this method should advance one channel, relative to the previous request, even if the prior request hasn’t yet completed. Adopt this method and replace the current player item with one that reflects the previous channel’s content, and call the completion block to dismiss the channel’s interstitial view.

> ❗ **Important**:  Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

 Only live video streams support channel skipping. This feature isn’t supported for VOD streams or local media.

## Parameters

- `playerViewController`: The player view controller.
- `completion`: A completion callback to invoke to dismiss the channel’s interstitial view.

## See Also

- [func playerViewController(AVPlayerViewController, skipToNextChannel: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptonextchannel:).md)
  Tells the delegate when the user wants to skip to the next channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](avplayerviewcontrollerdelegate/nextchannelinterstitialviewcontroller(for:).md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [func previousChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for:).md)
  Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptopreviouschannel:))*