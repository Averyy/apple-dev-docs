# init(label:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 14.0+ - Deprecated in 27.2 (renamed: GroupBox(content:label:))
- iPadOS 14.0+ - Deprecated in 27.2 (renamed: GroupBox(content:label:))
- Mac Catalyst 14.0+ - Deprecated in 27.2 (renamed: GroupBox(content:label:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: GroupBox(content:label:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: GroupBox(content:label:))

## Declaration

```swift
nonisolated
init(label: Label, @ContentBuilder content: () -> Content)
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

## See Also

### Creating a group box
- [init(content: () -> Content)](./init%28content%29.md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a group box with the provided label and view content.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a group box with the provided view content and title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(label:content:))*