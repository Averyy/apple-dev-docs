# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

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

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `content`: A group of menu items.

## See Also

- [init(content: () -> Content, label: () -> Label)](menu/init(content:label:).md)
  Creates a menu with a custom label.
- [init(_:image:content:)](menu/init(_:image:content:).md)
  Creates a menu that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](menu/init(_:systemimage:content:).md)
  Creates a menu that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:))*