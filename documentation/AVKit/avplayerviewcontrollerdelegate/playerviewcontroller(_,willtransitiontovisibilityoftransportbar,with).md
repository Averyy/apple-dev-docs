# playerViewController(_:willTransitionToVisibilityOfTransportBar:with:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the transport bar’s visibility is about to change.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willTransitionToVisibilityOfTransportBar visible: Bool, with coordinator: any AVPlayerViewControllerAnimationCoordinator)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController willTransitionToVisibilityOfTransportBar:(BOOL) visible withAnimationCoordinator:(id<AVPlayerViewControllerAnimationCoordinator>) coordinator;
```

## Parameters

- `playerViewController`: The player view controller.
- `visible`: The transport bar’s new visibility.
- `coordinator`: The animation coordinator to use to synchronize animations with the transport bar visibility.

## See Also

### Responding to transport bar changes
- [protocol AVPlayerViewControllerAnimationCoordinator](../avplayerviewcontrolleranimationcoordinator.md)
  A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:))*