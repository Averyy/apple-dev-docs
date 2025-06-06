# KeyEquivalent

**Framework**: SwiftUI  
**Kind**: struct

Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct KeyEquivalent
```

#### Overview

Key equivalents are used to establish keyboard shortcuts to app functionality. Any key can be used as a key equivalent as long as pressing it produces a single character value. Key equivalents are typically initialized using a single-character string literal, with constants for unprintable or hard-to-type values.

The modifier keys necessary to type a key equivalent are factored in to the resulting keyboard shortcut. That is, a key equivalent whose raw value is the capitalized string “A” corresponds with the keyboard shortcut Command-Shift-A. The exact mapping may depend on the keyboard layout—for example, a key equivalent with the character value “}” produces a shortcut equivalent to Command-Shift-] on ANSI keyboards, but would produce a different shortcut for keyboard layouts where punctuation characters are in different locations.

## Topics

### Getting arrow keys
- [static let upArrow: KeyEquivalent](keyequivalent/uparrow.md)
  Up Arrow (U+F700)
- [static let downArrow: KeyEquivalent](keyequivalent/downarrow.md)
  Down Arrow (U+F701)
- [static let leftArrow: KeyEquivalent](keyequivalent/leftarrow.md)
  Left Arrow (U+F702)
- [static let rightArrow: KeyEquivalent](keyequivalent/rightarrow.md)
  Right Arrow (U+F703)
### Getting other special keys
- [static let clear: KeyEquivalent](keyequivalent/clear.md)
  Clear (U+F739)
- [static let delete: KeyEquivalent](keyequivalent/delete.md)
  Delete (U+0008)
- [static let deleteForward: KeyEquivalent](keyequivalent/deleteforward.md)
  Delete Forward (U+F728)
- [static let end: KeyEquivalent](keyequivalent/end.md)
  End (U+F72B)
- [static let escape: KeyEquivalent](keyequivalent/escape.md)
  Escape (U+001B)
- [static let home: KeyEquivalent](keyequivalent/home.md)
  Home (U+F729)
- [static let pageDown: KeyEquivalent](keyequivalent/pagedown.md)
  Page Down (U+F72D)
- [static let pageUp: KeyEquivalent](keyequivalent/pageup.md)
  Page Up (U+F72C)
- [static let `return`: KeyEquivalent](keyequivalent/return.md)
  Return (U+000D)
- [static let space: KeyEquivalent](keyequivalent/space.md)
  Space (U+0020)
- [static let tab: KeyEquivalent](keyequivalent/tab.md)
  Tab (U+0009)
### Creating a key equivalent
- [init(Character)](keyequivalent/init(_:).md)
  Creates a new key equivalent from the given character value.
- [var character: Character](keyequivalent/character.md)
  The character value that the key equivalent represents.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
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
- [struct KeyboardShortcut](keyboardshortcut.md)
  Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [struct EventModifiers](eventmodifiers.md)
  A set of key modifiers that you can add to a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyequivalent)*