# init(_:systemImage:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu with a custom primary action that generates its label from a localized string key and system image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, @ViewBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

## Parameters

- `titleKey`: The key for the link’s localized title, which describes   the contents of the menu.
- `systemImage`: The name of the image resource to lookup.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary   interaction with the menu.

## See Also

- [init(_:content:primaryAction:)](menu/init(_:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)](menu/init(content:label:primaryaction:).md)
  Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](menu/init(_:image:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:))*