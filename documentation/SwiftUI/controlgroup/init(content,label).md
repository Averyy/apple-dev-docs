# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init<C, L>(@ContentBuilder content: () -> C, @ContentBuilder label: () -> L) where Content == LabeledControlGroupContent<C, L>, C : View, L : View
```

Available when `Content` conforms to `View`.

## Parameters

- `content`: The content to display.
- `label`: A view that describes the purpose of the group.

## See Also

### Creating a control group
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a new ControlGroup with the specified children
- [init(_:content:)](./init%28_,content%29.md)
  Creates a new control group with the specified content that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(content:label:))*