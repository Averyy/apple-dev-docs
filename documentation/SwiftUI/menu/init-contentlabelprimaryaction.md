# init(content:label:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu with a custom primary action and custom label.

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
init(@ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label, primaryAction: @escaping () -> Void)
```

## Parameters

- `content`: A group of menu items.
- `label`: A view describing the content of the menu.
- `primaryAction`: The action to perform on primary   interaction with the menu.

## See Also

- [init(_:content:primaryAction:)](menu/init(_:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(_:image:content:primaryAction:)](menu/init(_:image:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(_:systemImage:content:primaryAction:)](menu/init(_:systemimage:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(content:label:primaryaction:))*