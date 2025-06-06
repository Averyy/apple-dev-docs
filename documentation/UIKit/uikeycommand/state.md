# state

**Framework**: UIKit  
**Kind**: property

The state of the key command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIMenuElement.State { get set }
```

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
- [struct UIKeyModifierFlags](uikeymodifierflags.md)
  Constants that indicate which modifier keys are pressed.
- [var discoverabilityTitle: String?](uikeycommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the key command.
- [var attributes: UIMenuElement.Attributes](uikeycommand/attributes.md)
  The attributes indicating the style of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/state)*