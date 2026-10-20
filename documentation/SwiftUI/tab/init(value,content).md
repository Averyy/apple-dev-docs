# init(value:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab that you can use in a tab view, with an empty label.

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
nonisolated
init(value: Value, @ContentBuilder content: () -> Content) where Label == EmptyView
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<V>(value: V, @ContentBuilder content: () -> Content) where Value == V?, Label == EmptyView, V : Hashable
```

## Parameters

- `value`: The `selection` value which selects this tab.
- `content`: The view content of the tab.

## See Also

### Creating a tab
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(role: TabRole?, content: () -> Content)](./init%28role,content%29.md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](./init%28value,role,content%29.md)
  Creates a new tab with a label inferred from the role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(value:content:))*