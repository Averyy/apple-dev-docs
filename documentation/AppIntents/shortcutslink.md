# ShortcutsLink

**Framework**: App Intents  
**Kind**: struct

A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct ShortcutsLink
```

#### Overview

You can create a button by calling the initializer with an additional closure, which gets called whenever the button is tapped before opening the Shortcuts app.

```swift
ShortcutsLink(action: handleTap)
    .shortcutsLinkStyle(.dark)
```

## Topics

### Initializers
- [init(action: () -> Void)](shortcutslink/init(action:).md)
  Creates a link that launches Shortcuts and then executes the specified closure.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class ShortcutsUIButton](shortcutsuibutton.md)
  A button that opens the current app’s page in the Shortcuts app.
- [struct ShortcutsLinkStyle](shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink)*