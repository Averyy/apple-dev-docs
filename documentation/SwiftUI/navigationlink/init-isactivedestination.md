# init(_:isActive:destination:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.

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
init(_ titleKey: LocalizedStringKey, isActive: Binding<Bool>, @ViewBuilder destination: () -> Destination)
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `isActive`: A binding to a Boolean value that indicates whether    is currently presented.
- `destination`: A view for the navigation link to present.

## See Also

- [init(isActive: Binding<Bool>, destination: () -> Destination, label: () -> Label)](navigationlink/init(isactive:destination:label:).md)
  Creates a navigation link that presents the destination view when active.
- [init(_:tag:selection:destination:)](navigationlink/init(_:tag:selection:destination:).md)
  Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.
- [init<V>(tag: V, selection: Binding<V?>, destination: () -> Destination, label: () -> Label)](navigationlink/init(tag:selection:destination:label:).md)
  Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:isactive:destination:))*