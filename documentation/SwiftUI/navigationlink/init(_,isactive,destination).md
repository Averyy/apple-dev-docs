# init(_:isActive:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Use [`init(_:value:)`](./init%28_,value%29-810b2.md) inside a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, isActive: Binding<Bool>, @ContentBuilder destination: () -> Destination)
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<S>(_ title: S, isActive: Binding<Bool>, @ContentBuilder destination: () -> Destination) where S : StringProtocol
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `isActive`: A binding to a Boolean value that indicates whether `destination` is currently presented.
- `destination`: A view for the navigation link to present.

## See Also

### Creating links with content builders
- [init(isActive: Binding<Bool>, destination: () -> Destination, label: () -> Label)](./init%28isactive,destination,label%29.md)
  Creates a navigation link that presents the destination view when active.
- [init(_:tag:selection:destination:)](./init%28_,tag,selection,destination%29.md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](./init%28tag,selection,destination,label%29.md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:isactive:destination:))*