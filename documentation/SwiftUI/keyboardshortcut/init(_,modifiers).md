# init(_:modifiers:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(_ key: KeyEquivalent, modifiers: EventModifiers = .command)
```

#### Discussion

The localization configuration defaults to [`automatic`](keyboardshortcut/localization-swift.struct/automatic.md).

## See Also

- [var key: KeyEquivalent](keyboardshortcut/key.md)
  The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.
- [var modifiers: EventModifiers](keyboardshortcut/modifiers.md)
  The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut/init(_:modifiers:))*