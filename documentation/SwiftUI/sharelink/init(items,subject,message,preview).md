# init(items:subject:message:preview:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that presents the share interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(items: Data, subject: Text? = nil, message: Text? = nil, preview: @escaping (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>)
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label` is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

## Discussion

Use this initializer when you want the system-standard appearance for `ShareLink`.

## Parameters

- `items`: The items to share.
- `subject`: A title for the items to show when sharing to activities that support a subject field.
- `message`: A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.
- `preview`: A closure that returns a representation of each item to render in a preview.

## See Also

### Sharing items with a preview
- [init(_:items:subject:message:preview:)](./init%28_,items,subject,message,preview%29.md)
  Creates an instance, with a custom label, that presents the share interface.
- [init(items: Data, subject: Text?, message: Text?, preview: (Data.Element) -> SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)](./init%28items,subject,message,preview,label%29.md)
  Creates an instance that presents the share interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(items:subject:message:preview:))*