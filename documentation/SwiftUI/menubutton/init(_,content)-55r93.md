# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu button with the specified title and content.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`Menu`](../menu.md) instead.

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubutton/init(_:content:)-55r93)*