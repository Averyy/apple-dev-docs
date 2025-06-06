# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init

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
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey`: The key for the link’s localized title, which describes   the contents of the menu.
- `systemImage`: The name of the image resource to lookup.
- `content`: A group of menu items.

## See Also

- [init(_:content:)](menu/init(_:content:).md)
  Creates a menu that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](menu/init(content:label:).md)
  Creates a menu with a custom label.
- [init(_:image:content:)](menu/init(_:image:content:).md)
  Creates a menu that generates its label from a localized string key and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:))*