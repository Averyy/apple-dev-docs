# NSMenu.PresentationStyle.palette

**Framework**: AppKit  
**Kind**: case

A menu presentation style where items to display align horizontally.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case palette
```

#### Discussion

You can turn any menu into a palette menu by setting the menu’s presentation style to `.palette`. For each menu item, set its image. For template images, AppKit automatically adds the appropriate selection tint. Alternatively you can set the [`offStateImage`](nsmenuitem/offstateimage.md) and the [`onStateImage`](nsmenuitem/onstateimage.md). Use the `onStateImage` to indicate selection.

The following example creates a presentation style menu that displays a list of sport images. When a menu item selects, the system automatically tints the image.

![A palette style menu that expands to the right from a selected sports menu item listing a series of sport images horizonally. The second item in the list is tinted indicating selection.](https://docs-assets.developer.apple.com/published/8563e34565a1851e905ce287868a8bb1/media-4304532%402x.png)

## See Also

- [NSMenu.PresentationStyle.regular](nsmenu/presentationstyle-swift.enum/regular.md)
  The default presentation style for a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/presentationstyle-swift.enum/palette)*