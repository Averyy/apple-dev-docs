# AVPlayerViewControllerAnimationCoordinator

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
protocol AVPlayerViewControllerAnimationCoordinator : NSObjectProtocol
```

## Topics

### Coordinating Animations
- [func addCoordinatedAnimations((() -> Void)?, completion: ((Bool) -> Void)?)](avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(_:completion:).md)
  Adds animations to perform alongside the playback controls’ visibility animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func playerViewController(AVPlayerViewController, willTransitionToVisibilityOfTransportBar: Bool, with: any AVPlayerViewControllerAnimationCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:).md)
  Tells the delegate when the transport bar’s visibility is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator)*