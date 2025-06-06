# init(_:tag:selection:destination:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init<S, V>(_ title: S, tag: V, selection: Binding<V?>, @ViewBuilder destination: () -> Destination) where S : StringProtocol, V : Hashable
```

## Parameters

- `title`: A string for creating a text label.
- `tag`: The value of   that causes the link to present   .
- `selection`: A bound variable that causes the link to present    when   becomes equal to  .
- `destination`: A view for the navigation link to present.

## See Also

- [init(_:isActive:destination:)](navigationlink/init(_:isactive:destination:).md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(isActive: Binding<Bool>, destination: () -> Destination, label: () -> Label)](navigationlink/init(isactive:destination:label:).md)
  Creates a navigation link that presents the destination view when active.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](navigationlink/init(tag:selection:destination:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:tag:selection:destination:))*