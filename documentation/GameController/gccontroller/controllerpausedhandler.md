# controllerPausedHandler

**Framework**: Game Controller  
**Kind**: property

The block that the framework calls when the user presses the pause button on the controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var controllerPausedHandler: ((GCController) -> Void)? { get set }
```

#### Discussion

Implement this handler to toggle between pausing and resuming gameplay. Provide an interface that displays when the user pauses the game, and allows the user to resume gameplay. If your game suspends gameplay for some other reason, also implement this handler to resume gameplay when it’s possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/controllerpausedhandler)*