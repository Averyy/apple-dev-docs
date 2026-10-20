# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group box with the provided label and view content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content`: A [`ContentBuilder`](../contentbuilder.md) that produces the content for the group box.
- `label`: A [`ContentBuilder`](../contentbuilder.md) that produces a label for the group box.

## See Also

### Creating a group box
- [init(content: () -> Content)](./init%28content%29.md)
  Creates an unlabeled group box with the provided view content.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a group box with the provided view content and title.
- [init(label: Label, content: () -> Content)](./init%28label,content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(content:label:))*