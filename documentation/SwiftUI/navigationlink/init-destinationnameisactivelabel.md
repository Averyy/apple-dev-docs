# init(destinationName:isActive:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a view from a WatchKit storyboard when active.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(destinationName: String, isActive: Binding<Bool>, @ViewBuilder label: () -> Label)
```

## Parameters

- `destinationName`: The storyboard name of a view for the navigation   link to present.
- `isActive`: A binding to a Boolean value that indicates whether    is currently presented.
- `label`: A view builder to produce a label describing the    to present.

## See Also

- [init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destinationname:tag:selection:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.
- [init(destinationName: String, label: () -> Label)](navigationlink/init(destinationname:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:isactive:label:))*