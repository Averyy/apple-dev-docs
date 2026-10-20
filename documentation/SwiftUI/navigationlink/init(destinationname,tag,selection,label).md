# init(destinationName:tag:selection:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(value:label:)`](./init%28value,label%29-3qb8y.md) inside a [`List`](../list.md) within a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
init<V>(destinationName: String, tag: V, selection: Binding<V?>, @ContentBuilder label: () -> Label) where V : Hashable
```

Available when `Label` conforms to `View` and `Destination` is `_WKStoryboardContent`.

## Parameters

- `destinationName`: The storyboard name of a view for the navigation link to present.
- `tag`: The value of `selection` that causes the link to present `destination`.
- `selection`: A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.
- `label`: A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit
- [init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)](./init%28destinationname,isactive,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard when active.
- [init(destinationName: String, label: () -> Label)](./init%28destinationname,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:tag:selection:label:))*