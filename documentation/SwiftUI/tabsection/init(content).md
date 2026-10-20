# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(@TabContentBuilder<SelectionValue> content: () -> Content) where Header == EmptyView, Footer == EmptyView
```

Available when `Content` conforms to `TabContent` and `SelectionValue` conforms to `Hashable`.

**Other overloads**:

```swift
init<V>(@TabContentBuilder<V?> content: () -> Content) where Header == EmptyView, Footer == EmptyView, SelectionValue == V?, V : Hashable
```

## Parameters

- `content`: The section’s content.

## See Also

### Creating a tab section
- [init(_:content:)](./init%28_,content%29.md)
  Creates a section with the provided content.
- [init(content:header:)](./init%28content,header%29.md)
  Creates a section with a header and the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection/init(content:))*