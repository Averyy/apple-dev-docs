# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unlabeled group box with the provided view content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder content: () -> Content)
```

Available when `Label` is `EmptyView` and `Content` conforms to `View`.

## Parameters

- `content`: A [`ContentBuilder`](../contentbuilder.md) that produces the content for the group box.

## See Also

### Creating a group box
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a group box with the provided label and view content.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a group box with the provided view content and title.
- [init(label: Label, content: () -> Content)](./init%28label,content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(content:))*