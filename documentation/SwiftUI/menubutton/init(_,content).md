# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu button with the specified localized title and content.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`Menu`](../menu.md) instead.

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## See Also

### Creating a menu button
- [init(label: Label, content: () -> Content)](./init%28label,content%29.md)
  Creates a menu button with the specified label and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubutton/init(_:content:))*