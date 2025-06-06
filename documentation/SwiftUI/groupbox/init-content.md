# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group box with the provided view content and title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey`: The key for the group box’s title, which describes the   content of the group box.
- `content`: A   that produces the content for the   group box.

## See Also

- [init(content: () -> Content)](groupbox/init(content:).md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](groupbox/init(content:label:).md)
  Creates a group box with the provided label and view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(_:content:))*