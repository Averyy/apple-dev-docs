# buttonShare

**Framework**: Game Controller  
**Kind**: property

The share button on an Xbox Series X|S controller or later.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var buttonShare: GCControllerButtonInput? { get }
```

#### Discussion

The system reserves the Share button for screenshot and video recording gestures. If you want to disable these gestures in your app, set the button’s [`preferredSystemGestureState`](gccontrollerelement/preferredsystemgesturestate.md) to [`GCControllerElement.SystemGestureState.disabled`](gccontrollerelement/systemgesturestate/disabled.md).

## See Also

- [var paddleButton1: GCControllerButtonInput?](gcxboxgamepad/paddlebutton1.md)
  The controller’s paddle 1 button element, which has a P1 label on the back of the controller.
- [var paddleButton2: GCControllerButtonInput?](gcxboxgamepad/paddlebutton2.md)
  The paddle 2 button element, which has a P2 label on the back of the controller.
- [var paddleButton3: GCControllerButtonInput?](gcxboxgamepad/paddlebutton3.md)
  The paddle 3 button element, which has a P3 label on the back of the controller.
- [var paddleButton4: GCControllerButtonInput?](gcxboxgamepad/paddlebutton4.md)
  The paddle 4 button element, which has a P4 label on the back of the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcxboxgamepad/buttonshare)*