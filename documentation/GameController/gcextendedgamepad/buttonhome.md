# buttonHome

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The main menu button element that players use to enter the secondary menu and pause the game.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var buttonHome: GCControllerButtonInput? { get }
```

```objc
@property (nonatomic, readonly, nullable) GCControllerButtonInput * buttonHome;
```

#### Discussion

If the system doesn’t process the main menu events, it passes the events to your app.

## See Also

### Getting face button inputs
- [var buttonMenu: GCControllerButtonInput](./buttonmenu.md)
  The primary menu button element that players use to enter the main menu and pause the game.
- [var buttonOptions: GCControllerButtonInput?](./buttonoptions.md)
  The controller’s secondary menu button element.
- [var buttonA: GCControllerButtonInput](./buttona.md)
  The bottom face button that uses *A* or another indicator as its label.
- [var buttonB: GCControllerButtonInput](./buttonb.md)
  The right face button that uses *B* or another indicator as its label.
- [var buttonX: GCControllerButtonInput](./buttonx.md)
  The left face button that uses *X* or another indicator as its label.
- [var buttonY: GCControllerButtonInput](./buttony.md)
  The top face button that uses *Y* or another indicator as its label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/buttonhome)*