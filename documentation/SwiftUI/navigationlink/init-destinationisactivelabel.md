# init(destination:isActive:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents the destination view when active.

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
init(destination: Destination, isActive: Binding<Bool>, @ViewBuilder label: () -> Label)
```

## Parameters

- `destination`: A view for the navigation link to present.
- `isActive`: A binding to a Boolean value that indicates whether    is currently presented.
- `label`: A view builder to produce a label describing the    to present.

## See Also

- [init(_:destination:isActive:)](navigationlink/init(_:destination:isactive:).md)
  Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.
- [init(_:destination:tag:selection:)](navigationlink/init(_:destination:tag:selection:).md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(destination: Destination, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destination:tag:selection:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:isactive:label:))*