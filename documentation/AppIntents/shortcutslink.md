# ShortcutsLink

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

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
- [init(action: () -> Void)](./shortcutslink/init%28action%29.md)
  Creates a link that launches Shortcuts and then executes the specified closure.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Buttons
- [class ShortcutsUIButton](./shortcutsuibutton.md)
  A button that opens the current app’s page in the Shortcuts app.
- [struct ShortcutsLinkStyle](./shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink)*