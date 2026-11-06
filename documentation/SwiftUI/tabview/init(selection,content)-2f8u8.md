# init(selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+ - Deprecated in 27.3
- iPadOS 13.0+ - Deprecated in 27.3
- Mac Catalyst 13.0+ - Deprecated in 27.3
- macOS 10.15+ - Deprecated in 27.3
- tvOS 13.0+ - Deprecated in 27.3
- visionOS 1.0+
- watchOS 7.0+ - Deprecated in 27.3

> **Deprecated**: Use TabContentBuilder-based TabView initializers instead

## Declaration

```swift
nonisolated
init(selection: Binding<SelectionValue>?, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
nonisolated
init<C>(selection: Binding<SelectionValue>, @TabContentBuilder<SelectionValue> content: () -> C) where Content == TabContentBuilder<SelectionValue>.Content<C>, C : TabContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabview/init(selection:content:)-2f8u8)*