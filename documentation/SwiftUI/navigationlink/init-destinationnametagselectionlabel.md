# init(destinationName:tag:selection:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
init<V>(destinationName: String, tag: V, selection: Binding<V?>, @ContentBuilder label: () -> Label) where V : Hashable
```

## Parameters

- `destinationName`: The storyboard name of a view for the navigation link to present.
- `tag`: The value of `selection` that causes the link to present `destination`.
- `selection`: A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.
- `label`: A content builder to produce a label describing the `destination` to present.

## See Also

- [init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)](navigationlink/init(destinationname:isactive:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard when active.
- [init(destinationName: String, label: () -> Label)](navigationlink/init(destinationname:label:).md)
  Creates a navigation link that presents a view from a WatchKit storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:tag:selection:label:))*