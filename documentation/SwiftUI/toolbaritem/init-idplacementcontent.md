# init(id:placement:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toolbar item with the specified placement and content, which allows for user customization.

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
init(id: String, placement: ToolbarItemPlacement = .automatic, @ViewBuilder content: () -> Content)
```

## Parameters

- `id`: A unique identifier for this item.
- `placement`: Which section of the toolbar   the item should be placed in.
- `content`: The content of the item.

## See Also

- [init(placement: ToolbarItemPlacement, content: () -> Content)](toolbaritem/init(placement:content:).md)
  Creates a toolbar item with the specified placement and content.
- [init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool, content: () -> Content)](toolbaritem/init(id:placement:showsbydefault:content:).md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritem/init(id:placement:content:))*