# TCControlLabel

**Framework**: Touch Controller  
**Kind**: class

A label you associate with a touch control and provides a semantic description.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCControlLabel
```

## Topics

### Creating a control label
- [init(name: String, role: TCControlLabel.Role)](tccontrollabel/init(name:role:).md)
  Creates a new instance with the provided name and type.
### Inspecting the control
- [var role: TCControlLabel.Role](tccontrollabel/role-swift.property.md)
  The type of the control label.
- [TCControlLabel.Role](tccontrollabel/role-swift.enum.md)
  Defines the role for a control label. This determines the type of control on the touch controller’s associated GCController.
- [TCControlLabel.Role](tccontrollabel/role-swift.enum.md)
  Defines the role for a control label. This determines the type of control on the touch controller’s associated GCController.
### Accessing the controls
- [class var buttonA: TCControlLabel](tccontrollabel/buttona.md)
  Creates a pre-configured label for the “A” button.
- [class var buttonB: TCControlLabel](tccontrollabel/buttonb.md)
  Creates a pre-configured label for the “B” button.
- [class var buttonLeftShoulder: TCControlLabel](tccontrollabel/buttonleftshoulder.md)
  Creates a pre-configured label for the left shoulder button.
- [class var buttonLeftTrigger: TCControlLabel](tccontrollabel/buttonlefttrigger.md)
  Creates a pre-configured label for the left trigger button.
- [class var buttonMenu: TCControlLabel](tccontrollabel/buttonmenu.md)
  Creates a pre-configured label for the “Menu” button.
- [class var buttonOptions: TCControlLabel](tccontrollabel/buttonoptions.md)
  Creates a pre-configured label for the “Options” button.
- [class var buttonRightShoulder: TCControlLabel](tccontrollabel/buttonrightshoulder.md)
  Creates a pre-configured label for the right shoulder button.
- [class var buttonRightTrigger: TCControlLabel](tccontrollabel/buttonrighttrigger.md)
  Creates a pre-configured label for the right trigger button.
- [class var buttonX: TCControlLabel](tccontrollabel/buttonx.md)
  Creates a pre-configured label for the “X” button.
- [class var buttonY: TCControlLabel](tccontrollabel/buttony.md)
  Creates a pre-configured label for the “Y” button.
- [class var directionPad: TCControlLabel](tccontrollabel/directionpad.md)
  Creates a pre-configured label for the direction pad.
- [class var leftThumbstick: TCControlLabel](tccontrollabel/leftthumbstick.md)
  Creates a pre-configured label for the left thumbstick.
- [class var leftThumbstickButton: TCControlLabel](tccontrollabel/leftthumbstickbutton.md)
  Creates a pre-configured label for the left thumbstick button.
- [class var rightThumbstick: TCControlLabel](tccontrollabel/rightthumbstick.md)
  Creates a pre-configured label for the right thumbstick.
- [class var rightThumbstickButton: TCControlLabel](tccontrollabel/rightthumbstickbutton.md)
  Creates a pre-configured label for the right thumbstick button.
### Instance Properties
- [var name: String](tccontrollabel/name.md)
  The name of the control label that you use for lookup on a game controller instance.

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

- [var isEnabled: Bool](tccontrol/isenabled.md)
  A Boolean value that indicates whether the control is enabled.
- [var highlightDuration: TimeInterval](tccontrol/highlightduration.md)
  The duration of the highlight animation.
- [var label: TCControlLabel](tccontrol/label.md)
  The label associated with the control.
- [var isPressed: Bool](tccontrol/ispressed.md)
  Indicates whether the control is currently pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollabel)*