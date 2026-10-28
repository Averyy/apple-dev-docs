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
init<V>(@TabContentBuilder<V?> content: () -> Content, @ContentBuilder header: () -> Header) where Header : View, Footer == EmptyView, SelectionValue == V?, V : Hashable
```

Available when `Content` conforms to `TabContent` and `SelectionValue` conforms to `Hashable`.

**Other overloads**:

```swift
init(@TabContentBuilder<SelectionValue> content: () -> Content, @ContentBuilder header: () -> Header) where Header : View, Footer == EmptyView
```

## Discussion

This initializer overload allows for non optional tab content to be passed into `content`, even if the selection value of the tab view is optional.

## Parameters

- `content`: The section’s content.
- `header`: A view to use as the section’s header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection/init(content:header:)-3lrv1)*