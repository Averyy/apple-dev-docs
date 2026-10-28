# buttonOptions

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The controller’s secondary menu button element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var buttonOptions: GCControllerButtonInput? { get }
```

```objc
@property (nonatomic, readonly, nullable) GCControllerButtonInput * buttonOptions;
```

## Discussion

You can use the secondary menu to configure graphics and sound, and to pause the game.

## See Also

### Getting face button inputs
- [var buttonMenu: GCControllerButtonInput](./buttonmenu.md)
  The primary menu button element that players use to enter the main menu and pause the game.
- [var buttonHome: GCControllerButtonInput?](./buttonhome.md)
  The main menu button element that players use to enter the secondary menu and pause the game.
- [var buttonA: GCControllerButtonInput](./buttona.md)
  The bottom face button that uses *A* or another indicator as its label.
- [var buttonB: GCControllerButtonInput](./buttonb.md)
  The right face button that uses *B* or another indicator as its label.
- [var buttonX: GCControllerButtonInput](./buttonx.md)
  The left face button that uses *X* or another indicator as its label.
- [var buttonY: GCControllerButtonInput](./buttony.md)
  The top face button that uses *Y* or another indicator as its label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/buttonoptions)*