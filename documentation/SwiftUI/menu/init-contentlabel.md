# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu with a custom label.

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
init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content`: A group of menu items.
- `label`: A view describing the content of the menu.

## See Also

- [init(_:content:)](menu/init(_:content:).md)
  Creates a menu that generates its label from a localized string resource.
- [init(_:image:content:)](menu/init(_:image:content:).md)
  Creates a menu that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](menu/init(_:systemimage:content:).md)
  Creates a menu that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(content:label:))*