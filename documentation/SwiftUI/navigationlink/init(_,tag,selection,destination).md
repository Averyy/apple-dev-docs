# init(_:tag:selection:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Use [`init(_:value:)`](./init%28_,value%29-9ziux.md) inside a [`List`](../list.md) within a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
@export(implementation)
nonisolated init<S, V>(_ title: S, tag: V, selection: Binding<V?>, @ContentBuilder destination: () -> Destination) where S : StringProtocol, V : Hashable
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(_ titleKey: LocalizedStringKey, tag: V, selection: Binding<V?>, @ContentBuilder destination: () -> Destination) where V : Hashable
```

## Parameters

- `title`: A string for creating a text label.
- `tag`: The value of `selection` that causes the link to present `destination`.
- `selection`: A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.
- `destination`: A view for the navigation link to present.

## See Also

### Creating links with content builders
- [init(_:isActive:destination:)](./init%28_,isactive,destination%29.md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(isActive: Binding<Bool>, destination: () -> Destination, label: () -> Label)](./init%28isactive,destination,label%29.md)
  Creates a navigation link that presents the destination view when active.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](./init%28tag,selection,destination,label%29.md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:tag:selection:destination:))*