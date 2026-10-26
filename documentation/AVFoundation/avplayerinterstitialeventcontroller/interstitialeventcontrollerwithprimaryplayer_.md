# interstitialEventControllerWithPrimaryPlayer:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

A convenience initializer that creates an event controller with a player item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
+ (instancetype) interstitialEventControllerWithPrimaryPlayer:(AVPlayer *) primaryPlayer;
```

## Parameters

- `primaryPlayer`: A player that plays primary content. The system raises an exception you specify an interstitial player for this argument.

## See Also

### Creating an event controller
- [init(primaryPlayer: AVPlayer)](./init%28primaryplayer%29.md)
  Creates an event controller with a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/interstitialeventcontrollerwithprimaryplayer:)*