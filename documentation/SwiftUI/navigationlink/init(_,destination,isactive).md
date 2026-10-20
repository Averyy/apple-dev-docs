# init(_:destination:isActive:)

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

> **Deprecated**: Use [`init(_:value:)`](./init%28_,value%29-810b2.md) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<S>(_ title: S, destination: Destination, isActive: Binding<Bool>) where S : StringProtocol
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `destination`: A view for the navigation link to present.
- `isActive`: A binding to a Boolean value that indicates whether `destination` is currently presented.

## See Also

### Creating links with view arguments
- [init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)](./init%28destination,isactive,label%29.md)
  Creates a navigation link that presents the destination view when active.
- [init(_:destination:tag:selection:)](./init%28_,destination,tag,selection%29.md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: () -> Label)](./init%28destination,tag,selection,label%29.md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:isactive:))*