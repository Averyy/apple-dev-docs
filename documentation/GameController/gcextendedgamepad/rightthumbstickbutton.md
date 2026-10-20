# rightThumbstickButton

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The button on the right thumbstick of the controller.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- macOS 10.14.1+
- tvOS 12.1+
- visionOS 1.0+

## Declaration

```swift
var rightThumbstickButton: GCControllerButtonInput? { get }
```

```objc
@property (nonatomic, readonly, nullable) GCControllerButtonInput * rightThumbstickButton;
```

#### Discussion

If the thumbstick has a clickable component, this is a digital button.

## See Also

### Getting thumbstick and thumbstick button inputs
- [var leftThumbstick: GCControllerDirectionPad](./leftthumbstick.md)
  The controller’s left thumbstick element.
- [var rightThumbstick: GCControllerDirectionPad](./rightthumbstick.md)
  The controller’s right thumbstick element.
- [var leftThumbstickButton: GCControllerButtonInput?](./leftthumbstickbutton.md)
  The button on the left thumbstick of the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/rightthumbstickbutton)*