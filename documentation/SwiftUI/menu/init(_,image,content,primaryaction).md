# init(_:image:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu with a custom primary action that generates its label from a localized string resource.

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
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `image`: The name of the image resource to lookup.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action
- [init(_:content:primaryAction:)](./init%28_,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)](./init%28content,label,primaryaction%29.md)
  Creates a menu with a custom primary action and custom label.
- [init(_:systemImage:content:primaryAction:)](./init%28_,systemimage,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:image:content:primaryaction:))*