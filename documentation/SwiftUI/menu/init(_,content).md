# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu that generates its label from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content) where Label == Text
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content) where Label == Text
```

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where Label == Text, S : StringProtocol
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `content`: A group of menu items.

## See Also

### Creating a menu from content
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a menu with a custom label.
- [init(_:image:content:)](./init%28_,image,content%29.md)
  Creates a menu that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](./init%28_,systemimage,content%29.md)
  Creates a menu that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:))*