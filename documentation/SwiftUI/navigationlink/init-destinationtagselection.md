# init(_:destination:tag:selection:)

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
init<S, V>(_ title: S, destination: Destination, tag: V, selection: Binding<V?>) where S : StringProtocol, V : Hashable
```

## Parameters

- `title`: A string for creating a text label.
- `destination`: A view for the navigation link to present.
- `tag`: The value of   that causes the link to present   .
- `selection`: A bound variable that causes the link to present    when   becomes equal to  .

## See Also

- [init(_:destination:isActive:)](navigationlink/init(_:destination:isactive:).md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(destination: Destination, isActive: Binding<Bool>, label: () -> Label)](navigationlink/init(destination:isactive:label:).md)
  Creates a navigation link that presents the destination view when active.
- [init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destination:tag:selection:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:tag:selection:))*