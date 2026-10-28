# controllerPausedHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The block that the framework calls when the user presses the pause button on the controller.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Instead use the Menu button found on the controller’s profile, if it exists.

## Declaration

```swift
var controllerPausedHandler: ((GCController) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^controllerPausedHandler)(GCController *controller);
```

## Discussion

Implement this handler to toggle between pausing and resuming gameplay. Provide an interface that displays when the user pauses the game, and allows the user to resume gameplay. If your game suspends gameplay for some other reason, also implement this handler to resume gameplay when it’s possible.

## See Also

### Responding to a paused controller or controller event
- [protocol GCGameControllerSceneDelegate](../gcgamecontrollerscenedelegate.md)
- [class GCEventInteraction](../gceventinteraction.md)
  An interaction that indicates the view’s intent to receive game controller events through the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/controllerpausedhandler)*