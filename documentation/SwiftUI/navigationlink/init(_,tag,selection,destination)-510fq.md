# init(_:tag:selection:destination:)

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
@export(implementation)
nonisolated init<V>(_ titleKey: LocalizedStringKey, tag: V, selection: Binding<V?>, @ContentBuilder destination: () -> Destination) where V : Hashable
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<S, V>(_ title: S, tag: V, selection: Binding<V?>, @ContentBuilder destination: () -> Destination) where S : StringProtocol, V : Hashable
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `tag`: The value of `selection` that causes the link to present `destination`.
- `selection`: A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.
- `destination`: A view for the navigation link to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:tag:selection:destination:)-510fq)*