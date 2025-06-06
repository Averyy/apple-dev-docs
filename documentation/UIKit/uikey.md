# UIKey

**Framework**: UIKit  
**Kind**: class

An object that provides information about the state of a keyboard key.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIKey
```

#### Overview

[`UIKey`](uikey.md) provides relevant information about the current state of a key on a keyboard as a user presses and releases the key. To learn more, see [`Handling key presses made on a physical keyboard`](handling-key-presses-made-on-a-physical-keyboard.md).

## Topics

### Determining key type
- [var keyCode: UIKeyboardHIDUsage](uikey/keycode.md)
  The HID usage code of the key.
- [var modifierFlags: UIKeyModifierFlags](uikey/modifierflags.md)
  The modifier keys pressed and held while the user presses the key.
### Getting key characters
- [var characters: String](uikey/characters.md)
  A string that represents the text value of the key combined with any active modifier keys.
- [var charactersIgnoringModifiers: String](uikey/charactersignoringmodifiers.md)
  A string that represents the text value of the key without modifier keys.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)
  Detect when someone presses and releases keys on a physical keyboard.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding hardware keyboard support to your app](adding-hardware-keyboard-support-to-your-app.md)
  Enhance interactions with your app by handling raw keyboard events, writing custom keyboard shortcuts, and working with gesture recognizers.
- [enum UIKeyboardHIDUsage](uikeyboardhidusage.md)
  A set of HID usage codes that identify the keys of a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikey)*