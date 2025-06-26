# TCControlLabel

**Framework**: Touch Controller  
**Kind**: class

A label you associate with a touch control and provides a semantic description.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCControlLabel
```

## Topics

### Inspecting the control
- [var name: String](tccontrollabel/name.md)
  The name of the control label that you use for lookup on a game controller instance.
- [var type: TCControlLabelType](tccontrollabel/type.md)
  The type of the control label.
- [enum TCControlLabelType](tccontrollabeltype.md)
  Defines the type of control label.
### Accessing the controls
- [class func buttonA() -> Self](tccontrollabel/buttona.md)
  Creates a pre-configured label for the “A” button.
- [class func buttonB() -> Self](tccontrollabel/buttonb.md)
  Creates a pre-configured label for the “B” button.
- [class func buttonLeftShoulder() -> Self](tccontrollabel/buttonleftshoulder.md)
  Creates a pre-configured label for the left shoulder button.
- [class func buttonLeftTrigger() -> Self](tccontrollabel/buttonlefttrigger.md)
  Creates a pre-configured label for the left trigger button.
- [class func buttonMenu() -> Self](tccontrollabel/buttonmenu.md)
  Creates a pre-configured label for the “Menu” button.
- [class func buttonOptions() -> Self](tccontrollabel/buttonoptions.md)
  Creates a pre-configured label for the “Options” button.
- [class func buttonRightShoulder() -> Self](tccontrollabel/buttonrightshoulder.md)
  Creates a pre-configured label for the right shoulder button.
- [class func buttonRightTrigger() -> Self](tccontrollabel/buttonrighttrigger.md)
  Creates a pre-configured label for the right trigger button.
- [class func buttonX() -> Self](tccontrollabel/buttonx.md)
  Creates a pre-configured label for the “X” button.
- [class func buttonY() -> Self](tccontrollabel/buttony.md)
  Creates a pre-configured label for the “Y” button.
- [class func directionPad() -> Self](tccontrollabel/directionpad.md)
  Creates a pre-configured label for the direction pad.
- [class func leftThumbstick() -> Self](tccontrollabel/leftthumbstick.md)
  Creates a pre-configured label for the left thumbstick.
- [class func leftThumbstickButton() -> Self](tccontrollabel/leftthumbstickbutton.md)
  Creates a pre-configured label for the left thumbstick button.
- [class func rightThumbstick() -> Self](tccontrollabel/rightthumbstick.md)
  Creates a pre-configured label for the right thumbstick.
- [class func rightThumbstickButton() -> Self](tccontrollabel/rightthumbstickbutton.md)
  Creates a pre-configured label for the right thumbstick button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var collider: any TCCollider](tccontrol/collider.md)
  The collider for the control.
- [var enabled: Bool](tccontrol/enabled.md)
  A Boolean value that indicates whether the control is enabled.
- [var highlightFactor: Float](tccontrol/highlightfactor.md)
  The factor by which to highlight the control when pressed.
- [var highlightTime: simd_float1](tccontrol/highlighttime.md)
  The duration of the highlight animation.
- [var label: TCControlLabel](tccontrol/label.md)
  The label associated with the control.
- [var pressed: Bool](tccontrol/pressed.md)
  Indicates whether the control is currently pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollabel)*