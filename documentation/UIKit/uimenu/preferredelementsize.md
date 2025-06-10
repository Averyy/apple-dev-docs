# preferredElementSize

**Framework**: UIKit  
**Kind**: property

The size of the menu’s child elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredElementSize: UIMenu.ElementSize { get set }
```

#### Discussion

This property allows you to choose between different layouts in the context menu:

- The [`UIMenu.ElementSize.small`](uimenu/elementsize/small.md) size gives the menu a more compact, side-by-side appearance, allowing you to fit more actions in a single row.
- The [`UIMenu.ElementSize.medium`](uimenu/elementsize/medium.md) size gives the menu the side-by-side appearance, but shows additional detail for each action. The text-editing menu uses this element size to display the standard edit menu.
- The [`UIMenu.ElementSize.large`](uimenu/elementsize/large.md) size gives the menu its default, full-width appearance.

![Screenshots of menus that use the small, medium, and large element sizes. The menu using the small size contains four side-by-side icons in the top row, followed by full-size elements. The menu using the medium size contains three side-by-side icons with labels in the top row, followed by full-size elements. The menu using the large size only contains full-size elements.](https://docs-assets.developer.apple.com/published/a740af48998156b0cedd75eee1958ab3/media-4047986%402x.png)

If you specify the [`UIMenu.ElementSize.small`](uimenu/elementsize/small.md) or [`UIMenu.ElementSize.medium`](uimenu/elementsize/medium.md) sizes, the menu displays any items beyond the first three (for medium) or four (for small) as full-size elements.

This property doesn’t have an effect if you build your app with Mac Catalyst.

> **Note**:  Session 10071: [`Adopt desktop-class editing interactions`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10071)

## See Also

- [UIMenu.ElementSize](uimenu/elementsize.md)
  Constants that determine the size of an element in a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize)*