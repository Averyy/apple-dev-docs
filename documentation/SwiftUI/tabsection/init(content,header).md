# init(content:header:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header and the provided section content.

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
init(@TabContentBuilder<SelectionValue> content: () -> Content, @ContentBuilder header: () -> Header) where Header : View, Footer == EmptyView
```

Available when `Content` conforms to `TabContent` and `SelectionValue` conforms to `Hashable`.

**Other overloads**:

```swift
init<V>(@TabContentBuilder<V?> content: () -> Content, @ContentBuilder header: () -> Header) where Header : View, Footer == EmptyView, SelectionValue == V?, V : Hashable
```

## Parameters

- `content`: The section’s content.
- `header`: A view to use as the section’s header.

## See Also

### Creating a tab section
- [init(content:)](./init%28content%29.md)
  Creates a section with the provided section content.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a section with the provided content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection/init(content:header:))*