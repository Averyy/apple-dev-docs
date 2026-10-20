# init(destinationName:isActive:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a view from a WatchKit storyboard when active.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(value:label:)`](./init%28value,label%29-3qb8y.md) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
init(destinationName: String, isActive: Binding<Bool>, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `Destination` is `_WKStoryboardContent`.

## Parameters

- `destinationName`: The storyboard name of a view for the navigation link to present.
- `isActive`: A binding to a Boolean value that indicates whether `destination` is currently presented.
- `label`: A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit
- [init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () -> Label)](./init%28destinationname,tag,selection,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.
- [init(destinationName: String, label: () -> Label)](./init%28destinationname,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:isactive:label:))*