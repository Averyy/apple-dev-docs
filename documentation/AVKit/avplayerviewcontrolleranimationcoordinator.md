# AVPlayerViewControllerAnimationCoordinator

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
protocol AVPlayerViewControllerAnimationCoordinator : NSObjectProtocol
```

```objc
@protocol AVPlayerViewControllerAnimationCoordinator <NSObject>
```

## Topics

### Coordinating animations
- [func addCoordinatedAnimations((() -> Void)?, completion: ((Bool) -> Void)?)](./avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations%28_,completion%29.md)
  Adds animations to perform alongside the playback controls’ visibility animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to transport bar changes
- [func playerViewController(AVPlayerViewController, willTransitionToVisibilityOfTransportBar: Bool, with: any AVPlayerViewControllerAnimationCoordinator)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willtransitiontovisibilityoftransportbar,with%29.md)
  Tells the delegate when the transport bar’s visibility is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator)*