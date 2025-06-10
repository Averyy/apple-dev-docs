# GCGameControllerSceneDelegate

**Framework**: Game Controller  
**Kind**: protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol GCGameControllerSceneDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func scene(UIScene, didActivateGameControllerWith: GCGameControllerActivationContext)](gcgamecontrollerscenedelegate/scene(_:didactivategamecontrollerwith:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var controllerPausedHandler: ((GCController) -> Void)?](gccontroller/controllerpausedhandler.md)
  The block that the framework calls when the user presses the pause button on the controller.
- [class GCEventInteraction](gceventinteraction.md)
  An interaction that indicates the view’s intent to receive game controller events through the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamecontrollerscenedelegate)*