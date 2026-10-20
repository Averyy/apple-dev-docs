# init(id:placement:showsByDefault:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toolbar item with the specified placement and content, which allows for user customization.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use the CustomizableToolbarContent/defaultCustomization(_:options) modifier with a value of .hidden

## Declaration

```swift
nonisolated
init(id: String, placement: ToolbarItemPlacement = .automatic, showsByDefault: Bool, @ContentBuilder content: () -> Content)
```

Available when `ID` is `String` and `Content` conforms to `View`.

## Parameters

- `id`: A unique identifier for this item.
- `placement`: Which section of the toolbar the item should be placed in.
- `showsByDefault`: Whether the item appears by default in the toolbar, or only shows if the user explicitly adds it via customization.
- `content`: The content of the item.

## See Also

### Creating a toolbar item
- [init(placement: ToolbarItemPlacement, content: () -> Content)](./init%28placement,content%29.md)
  Creates a toolbar item with the specified placement and content.
- [init(id: String, placement: ToolbarItemPlacement, content: () -> Content)](./init%28id,placement,content%29.md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritem/init(id:placement:showsbydefault:content:))*