# discoverabilityTitle

**Framework**: UIKit  
**Kind**: property

An elaborated title that explains the purpose of the key command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var discoverabilityTitle: String? { get set }
```

#### Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [`title`](uicommand/title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

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
- [var attributes: UIMenuElement.Attributes](uikeycommand/attributes.md)
  The attributes indicating the style of the key command.
- [var state: UIMenuElement.State](uikeycommand/state.md)
  The state of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/discoverabilitytitle)*