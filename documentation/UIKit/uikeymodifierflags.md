# UIKeyModifierFlags

**Framework**: UIKit  
**Kind**: struct

Constants that indicate which modifier keys are pressed.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct UIKeyModifierFlags
```

## Topics

### Modifier flags
- [static var alphaShift: UIKeyModifierFlags](uikeymodifierflags/alphashift.md)
  A modifier flag that indicates the user pressed the Caps Lock key.
- [static var shift: UIKeyModifierFlags](uikeymodifierflags/shift.md)
  A modifier flag that indicates the user pressed the Shift key.
- [static var control: UIKeyModifierFlags](uikeymodifierflags/control.md)
  A modifier flag that indicates the user pressed the Control key.
- [static var alternate: UIKeyModifierFlags](uikeymodifierflags/alternate.md)
  A modifier flag that indicates the user pressed the Option key.
- [static var command: UIKeyModifierFlags](uikeymodifierflags/command.md)
  A modifier flag that indicates the user pressed the Command key.
- [static var numericPad: UIKeyModifierFlags](uikeymodifierflags/numericpad.md)
  A modifier flag that indicates the user pressed a key located on the numeric keypad.
### Initializers
- [init(rawValue: Int)](uikeymodifierflags/init(rawvalue:).md)
  Creates a modifier-flags structure from data in an unarchiver.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var title: String](uikeycommand/title.md)
  The key command’s title.
- [var image: UIImage?](uikeycommand/image.md)
  The key command’s image.
- [var input: String?](uikeycommand/input.md)
  The string of characters corresponding to the keys that must be pressed to match this key command.
- [var action: Selector?](uikeycommand/action.md)
  The command’s action-method selector.
- [var modifierFlags: UIKeyModifierFlags](uikeycommand/modifierflags.md)
  The bit mask of modifier flags that must be pressed to match this key command.
- [var discoverabilityTitle: String?](uikeycommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the key command.
- [var attributes: UIMenuElement.Attributes](uikeycommand/attributes.md)
  The attributes indicating the style of the key command.
- [var state: UIMenuElement.State](uikeycommand/state.md)
  The state of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeymodifierflags)*