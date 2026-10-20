# init(destinationName:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a view from a WatchKit storyboard.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(destination:label:)`](./init%28destination,label%29-27n7s.md) instead.

## Declaration

```swift
nonisolated
init(destinationName: String, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `Destination` is `_WKStoryboardContent`.

## Parameters

- `destinationName`: The storyboard name of a view for the navigation link to present.
- `label`: A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit
- [init(destinationName: String, isActive: Binding<Bool>, label: () -> Label)](./init%28destinationname,isactive,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard when active.
- [init<V>(destinationName: String, tag: V, selection: Binding<V?>, label: () -> Label)](./init%28destinationname,tag,selection,label%29.md)
  Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:label:))*