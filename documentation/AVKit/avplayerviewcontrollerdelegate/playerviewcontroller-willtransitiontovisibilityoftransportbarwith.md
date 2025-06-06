# playerViewController(_:willTransitionToVisibilityOfTransportBar:with:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the transport bar’s visibility is about to change.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willTransitionToVisibilityOfTransportBar visible: Bool, with coordinator: any AVPlayerViewControllerAnimationCoordinator)
```

## Parameters

- `playerViewController`: The player view controller.
- `visible`: The transport bar’s new visibility.
- `coordinator`: The animation coordinator to use to synchronize animations with the transport bar visibility.

## See Also

- [protocol AVPlayerViewControllerAnimationCoordinator](avplayerviewcontrolleranimationcoordinator.md)
  A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:))*