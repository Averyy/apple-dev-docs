# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group box with the provided view content and title.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource`: Text resource for the group box’s title, which describes the content of the group box.
- `content`: A [`ContentBuilder`](contentbuilder.md) that produces the content for the group box.

## See Also

- [init(content: () -> Content)](groupbox/init(content:).md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](groupbox/init(content:label:).md)
  Creates a group box with the provided label and view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(_:content:))*