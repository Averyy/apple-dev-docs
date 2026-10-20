# init(content:label:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label, primaryAction: @escaping () -> Void)
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

## Parameters

- `content`: A group of menu items.
- `label`: A view describing the content of the menu.
- `primaryAction`: The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action
- [init(_:content:primaryAction:)](./init%28_,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:image:content:primaryAction:)](./init%28_,image,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:systemImage:content:primaryAction:)](./init%28_,systemimage,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(content:label:primaryaction:))*