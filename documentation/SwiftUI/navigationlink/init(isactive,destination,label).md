# init(isActive:destination:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents the destination view when active.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Use [`init(value:label:)`](./init%28value,label%29-3qb8y.md) inside a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
@export(implementation)
nonisolated init(isActive: Binding<Bool>, @ContentBuilder destination: () -> Destination, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `Destination` conforms to `View`.

## Parameters

- `isActive`: A binding to a Boolean value that indicates whether `destination` is currently presented.
- `destination`: A view for the navigation link to present.
- `label`: A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links with content builders
- [init(_:isActive:destination:)](./init%28_,isactive,destination%29.md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(_:tag:selection:destination:)](./init%28_,tag,selection,destination%29.md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](./init%28tag,selection,destination,label%29.md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(isactive:destination:label:))*