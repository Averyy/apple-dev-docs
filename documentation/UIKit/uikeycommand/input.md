# input

**Framework**: UIKit  
**Kind**: property

The string of characters corresponding to the keys that must be pressed to match this key command.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var input: String? { get }
```

## See Also

- [var title: String](uikeycommand/title.md)
  The key command’s title.
- [var image: UIImage?](uikeycommand/image.md)
  The key command’s image.
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
- [var state: UIMenuElement.State](uikeycommand/state.md)
  The state of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/input)*