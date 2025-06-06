# keyboardShortcut

**Framework**: SwiftUI  
**Kind**: property

The keyboard shortcut that buttons in this environment will be triggered with.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var keyboardShortcut: KeyboardShortcut? { get }
```

#### Discussion

This is particularly useful in button styles when a button’s appearance depends on the shortcut associated with it. On macOS, for example, when a button is bound to the Return key, it is typically drawn with a special emphasis. This happens automatically when using the built-in button styles, and can be implemented manually in custom styles using this environment key:

```swift
private struct MyButtonStyle: ButtonStyle {
    @Environment(\.keyboardShortcut)
    private var shortcut: KeyboardShortcut?

    func makeBody(configuration: Configuration) -> some View {
        let labelFont = Font.body
            .weight(shortcut == .defaultAction ? .bold : .regular)
        configuration.label
            .font(labelFont)
    }
}
```

If no keyboard shortcut has been applied to the view or its ancestor, then the environment value will be `nil`.

## See Also

- [func keyboardShortcut(_:)](view/keyboardshortcut(_:).md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](view/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](view/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [struct KeyboardShortcut](keyboardshortcut.md)
  Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [struct KeyEquivalent](keyequivalent.md)
  Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [struct EventModifiers](eventmodifiers.md)
  A set of key modifiers that you can add to a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/keyboardshortcut)*