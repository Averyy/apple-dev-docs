# init(destinationName:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a view from a WatchKit storyboard.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(destinationName: String, @ViewBuilder label: () -> Label)
```

## Parameters

- `destinationName`: The storyboard name of a view for the navigation   link to present.
- `label`: A view builder to produce a label describing the    to present.

## See Also

- [init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)](navigationlink/init(destinationname:isactive:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when active.
- [init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () -> Label)](navigationlink/init(destinationname:tag:selection:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:label:))*