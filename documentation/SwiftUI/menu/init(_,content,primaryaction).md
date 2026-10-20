# init(_:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` conforms to `View` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text
```

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text, S : StringProtocol
```

## Parameters

- `titleResource`: Text resource for the link’s localized title, which describes the contents of the menu.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary interaction with the menu.

## See Also

### Creating a menu with a primary action
- [init(content: () -> Content, label: () -> Label, primaryAction: () -> Void)](./init%28content,label,primaryaction%29.md)
  Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](./init%28_,image,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string resource.
- [init(_:systemImage:content:primaryAction:)](./init%28_,systemimage,content,primaryaction%29.md)
  Creates a menu with a custom primary action that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:primaryaction:))*