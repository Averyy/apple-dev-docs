# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu that generates its label from a localized string resource and image resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `image`: The name of the image resource to lookup.
- `content`: A group of menu items.

## See Also

### Creating a menu from content
- [init(_:content:)](./init%28_,content%29.md)
  Creates a menu that generates its label from a localized string resource.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a menu with a custom label.
- [init(_:systemImage:content:)](./init%28_,systemimage,content%29.md)
  Creates a menu that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:image:content:))*