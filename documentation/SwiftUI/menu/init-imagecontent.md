# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu that generates its label from a localized string key and image resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey`: The key for the link’s localized title, which describes   the contents of the menu.
- `image`: The name of the image resource to lookup.
- `content`: A group of menu items.

## See Also

- [init(_:content:)](menu/init(_:content:).md)
  Creates a menu that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](menu/init(content:label:).md)
  Creates a menu with a custom label.
- [init(_:systemImage:content:)](menu/init(_:systemimage:content:).md)
  Creates a menu that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:image:content:))*