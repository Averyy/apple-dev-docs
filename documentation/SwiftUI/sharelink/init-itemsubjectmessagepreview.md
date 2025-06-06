# init(_:item:subject:message:preview:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance, with a custom label, that presents the share interface.

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
init<I>(_ title: Text, item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, I : Transferable
```

## Parameters

- `title`: The title of the share action.
- `item`: The item to share.
- `subject`: A title for the item to show when sharing to activities   that support a subject field.
- `message`: A description of the item to show when sharing to   activities that support a message field. Activities may   support attributed text or HTML strings.
- `preview`: A representation of the item to render in a preview.

## See Also

- [init<I>(item: I, subject: Text?, message: Text?, preview: SharePreview<PreviewImage, PreviewIcon>)](sharelink/init(item:subject:message:preview:).md)
  Creates an instance that presents the share interface.
- [init<I>(item: I, subject: Text?, message: Text?, preview: SharePreview<PreviewImage, PreviewIcon>, label: () -> Label)](sharelink/init(item:subject:message:preview:label:).md)
  Creates an instance that presents the share interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:item:subject:message:preview:))*