# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group box with the provided label and view content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(@ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `content`: A   that produces the content for the   group box.
- `label`: A   that produces a label for the group   box.

## See Also

- [init(content: () -> Content)](groupbox/init(content:).md)
  Creates an unlabeled group box with the provided view content.
- [init(_:content:)](groupbox/init(_:content:).md)
  Creates a group box with the provided view content and title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(content:label:))*