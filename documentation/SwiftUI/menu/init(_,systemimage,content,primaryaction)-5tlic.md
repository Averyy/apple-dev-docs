# init(_:systemImage:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu with a custom primary action that generates its label from a localized string resource and system image.

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
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void)
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `systemImage`: The name of the image resource to lookup.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary interaction with the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:)-5tlic)*