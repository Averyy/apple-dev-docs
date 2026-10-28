# init(_:item:subject:message:preview:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init<S, I>(_ title: S, item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, S : StringProtocol, I : Transferable
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` conforms to `Transferable`, `PreviewIcon` conforms to `Transferable`, `Label` is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<I>(_ titleResource: LocalizedStringResource, item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, I : Transferable
```

```swift
nonisolated
init<I>(_ title: Text, item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, I : Transferable
```

```swift
nonisolated
init<I>(_ titleKey: LocalizedStringKey, item: I, subject: Text? = nil, message: Text? = nil, preview: SharePreview<PreviewImage, PreviewIcon>) where Data == CollectionOfOne<I>, I : Transferable
```

## Parameters

- `title`: The title of the share action.
- `item`: The item to share.
- `subject`: A title for the item to show when sharing to activities that support a subject field.
- `message`: A description of the item to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.
- `preview`: A representation of the item to render in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:item:subject:message:preview:)-9go2l)*