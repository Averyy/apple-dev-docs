# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Parameters

- `titleResource`: Text resource for the group box’s title, which describes the content of the group box.
- `content`: A [`ContentBuilder`](../contentbuilder.md) that produces the content for the group box.

## See Also

### Creating a group box
- [init(content: () -> Content)](./init%28content%29.md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a group box with the provided label and view content.
- [init(label: Label, content: () -> Content)](./init%28label,content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(_:content:))*