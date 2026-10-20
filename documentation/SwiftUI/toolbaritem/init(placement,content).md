# init(placement:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toolbar item with the specified placement and content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(placement: ToolbarItemPlacement = .automatic, @ContentBuilder content: () -> Content)
```

Available when `ID` is `()` and `Content` conforms to `View`.

## Parameters

- `placement`: Which section of the toolbar the item should be placed in.
- `content`: The content of the item.

## See Also

### Creating a toolbar item
- [init(id: String, placement: ToolbarItemPlacement, content: () -> Content)](./init%28id,placement,content%29.md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.
- [init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool, content: () -> Content)](./init%28id,placement,showsbydefault,content%29.md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritem/init(placement:content:))*