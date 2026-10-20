# GCGameControllerSceneDelegate

**Framework**: Game Controller  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
protocol GCGameControllerSceneDelegate : NSObjectProtocol
```

```objc
@protocol GCGameControllerSceneDelegate <NSObject>
```

## Topics

### Instance Methods
- [func scene(UIScene, didActivateGameControllerWith: GCGameControllerActivationContext)](./gcgamecontrollerscenedelegate/scene%28_,didactivategamecontrollerwith%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to a paused controller or controller event
- [var controllerPausedHandler: ((GCController) -> Void)?](./gccontroller/controllerpausedhandler.md)
  The block that the framework calls when the user presses the pause button on the controller.
- [class GCEventInteraction](./gceventinteraction.md)
  An interaction that indicates the view’s intent to receive game controller events through the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamecontrollerscenedelegate)*