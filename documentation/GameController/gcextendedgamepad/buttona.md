# buttonA

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The bottom face button that uses *A* or another indicator as its label.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var buttonA: GCControllerButtonInput { get }
```

```objc
@property (nonatomic, readonly) GCControllerButtonInput * buttonA;
```

## Discussion

The face buttons in the extended gamepad profile may be either analog or digital buttons.

## See Also

### Getting face button inputs
- [var buttonMenu: GCControllerButtonInput](./buttonmenu.md)
  The primary menu button element that players use to enter the main menu and pause the game.
- [var buttonOptions: GCControllerButtonInput?](./buttonoptions.md)
  The controller’s secondary menu button element.
- [var buttonHome: GCControllerButtonInput?](./buttonhome.md)
  The main menu button element that players use to enter the secondary menu and pause the game.
- [var buttonB: GCControllerButtonInput](./buttonb.md)
  The right face button that uses *B* or another indicator as its label.
- [var buttonX: GCControllerButtonInput](./buttonx.md)
  The left face button that uses *X* or another indicator as its label.
- [var buttonY: GCControllerButtonInput](./buttony.md)
  The top face button that uses *Y* or another indicator as its label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/buttona)*