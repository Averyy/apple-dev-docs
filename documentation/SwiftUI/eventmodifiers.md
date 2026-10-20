# EventModifiers

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A set of key modifiers that you can add to a gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct EventModifiers
```

## Topics

### Getting modifier keys
- [static let all: EventModifiers](./eventmodifiers/all.md)
  All possible modifier keys.
- [static let capsLock: EventModifiers](./eventmodifiers/capslock.md)
  The Caps Lock key.
- [static let command: EventModifiers](./eventmodifiers/command.md)
  The Command key.
- [static let control: EventModifiers](./eventmodifiers/control.md)
  The Control key.
- [static let numericPad: EventModifiers](./eventmodifiers/numericpad.md)
  Any key on the numeric keypad.
- [static let option: EventModifiers](./eventmodifiers/option.md)
  The Option key.
- [static let shift: EventModifiers](./eventmodifiers/shift.md)
  The Shift key.
- [static let function: EventModifiers](./eventmodifiers/function.md)
  The Function key.
### Creating a set of options
- [init(rawValue: Int)](./eventmodifiers/init%28rawvalue%29.md)
  Creates a new set from a raw value.
- [let rawValue: Int](./eventmodifiers/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Creating keyboard shortcuts
- [func keyboardShortcut(_:)](./view/keyboardshortcut%28_%29.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](./view/keyboardshortcut%28_,modifiers%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](./view/keyboardshortcut%28_,modifiers,localization%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [var keyboardShortcut: KeyboardShortcut?](./environmentvalues/keyboardshortcut.md)
  The keyboard shortcut that buttons in this environment will be triggered with.
- [struct KeyboardShortcut](./keyboardshortcut.md)
  Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [struct KeyEquivalent](./keyequivalent.md)
  Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/eventmodifiers)*