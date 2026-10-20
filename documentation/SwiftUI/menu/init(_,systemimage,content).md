# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu that generates its label from a localized string key and system image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Parameters

- `titleKey`: The key for the link’s localized title, which describes the contents of the menu.
- `systemImage`: The name of the image resource to lookup.
- `content`: A group of menu items.

## See Also

### Creating a menu from content
- [init(_:content:)](./init%28_,content%29.md)
  Creates a menu that generates its label from a localized string resource.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a menu with a custom label.
- [init(_:image:content:)](./init%28_,image,content%29.md)
  Creates a menu that generates its label from a localized string resource and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:))*