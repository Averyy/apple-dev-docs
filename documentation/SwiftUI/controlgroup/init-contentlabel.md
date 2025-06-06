# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new control group with the specified content and a label.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<C, L>(@ViewBuilder content: () -> C, @ViewBuilder label: () -> L) where Content == LabeledControlGroupContent<C, L>, C : View, L : View
```

## Parameters

- `content`: The content to display.
- `label`: A view that describes the purpose of the group.

## See Also

- [init(content: () -> Content)](controlgroup/init(content:).md)
  Creates a new ControlGroup with the specified children
- [init(_:content:)](controlgroup/init(_:content:).md)
  Creates a new control group with the specified content that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(content:label:))*