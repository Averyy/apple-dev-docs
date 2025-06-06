# KeyboardShortcut

**Framework**: SwiftUI  
**Kind**: struct

Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct KeyboardShortcut
```

## Topics

### Getting standard shortcuts
- [static let cancelAction: KeyboardShortcut](keyboardshortcut/cancelaction.md)
  The standard keyboard shortcut for cancelling the in-progress action or dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.
- [static let defaultAction: KeyboardShortcut](keyboardshortcut/defaultaction.md)
  The standard keyboard shortcut for the default button, consisting of the Return (↩) key and no modifiers.
### Creating a shortcut
- [init(KeyEquivalent, modifiers: EventModifiers)](keyboardshortcut/init(_:modifiers:).md)
  Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [var key: KeyEquivalent](keyboardshortcut/key.md)
  The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.
- [var modifiers: EventModifiers](keyboardshortcut/modifiers.md)
  The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.
### Creating a localized shortcut
- [init(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization)](keyboardshortcut/init(_:modifiers:localization:).md)
  Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [var localization: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.property.md)
  The localization strategy to apply to this shortcut.
- [KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct.md)
  Options for how a keyboard shortcut participates in automatic localization.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func keyboardShortcut(_:)](view/keyboardshortcut(_:).md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](view/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](view/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [var keyboardShortcut: KeyboardShortcut?](environmentvalues/keyboardshortcut.md)
  The keyboard shortcut that buttons in this environment will be triggered with.
- [struct KeyEquivalent](keyequivalent.md)
  Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [struct EventModifiers](eventmodifiers.md)
  A set of key modifiers that you can add to a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut)*