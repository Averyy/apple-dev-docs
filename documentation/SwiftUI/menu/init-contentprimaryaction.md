# init(_:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a menu with a custom primary action that generates its label from a localized string resource.

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
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary interaction with the menu.

## See Also

- [init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)](menu/init(content:label:primaryaction:).md)
  Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](menu/init(_:image:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:systemImage:content:primaryAction:)](menu/init(_:systemimage:content:primaryaction:).md)
  Creates a menu with a custom primary action that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:primaryaction:))*