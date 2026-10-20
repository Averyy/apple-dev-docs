# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new ControlGroup with the specified children

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content`: The children to display

## See Also

### Creating a control group
- [init<C, L>(content: () -> C, label: () -> L)](./init%28content,label%29.md)
  Creates a new control group with the specified content and a label.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a new control group with the specified content that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(content:))*