# init(_:modifiers:localization:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(_ key: KeyEquivalent, modifiers: EventModifiers = .command, localization: KeyboardShortcut.Localization)
```

#### Discussion

Use the `localization` parameter to specify a localization strategy for this shortcut.

## See Also

- [var localization: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.property.md)
  The localization strategy to apply to this shortcut.
- [KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct.md)
  Options for how a keyboard shortcut participates in automatic localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut/init(_:modifiers:localization:))*