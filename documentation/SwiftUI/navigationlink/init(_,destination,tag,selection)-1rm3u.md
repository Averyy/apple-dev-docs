# init(_:destination:tag:selection:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a localized string key.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Use [`init(_:value:)`](./init%28_,value%29-810b2.md) inside a [`List`](../list.md) within a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, destination: Destination, tag: V, selection: Binding<V?>) where V : Hashable
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<S, V>(_ title: S, destination: Destination, tag: V, selection: Binding<V?>) where S : StringProtocol, V : Hashable
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `destination`: A view for the navigation link to present.
- `tag`: The value of `selection` that causes the link to present `destination`.
- `selection`: A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:tag:selection:)-1rm3u)*