# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder content: () -> Content)
```

Available when `SelectionValue` is `Int` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<C>(@TabContentBuilder<Never> content: () -> C) where SelectionValue == Never, Content == TabContentBuilder<Never>.Content<C>, C : TabContent
```

## See Also

### Creating a tab view
- [init(selection:content:)](./init%28selection,content%29.md)
  Creates a tab view that uses a builder to create and specify selection values for its tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabview/init(content:))*