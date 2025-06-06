# separatorLayoutGuide

**Framework**: UIKit  
**Kind**: property

A guide for laying out separators in relation to the primary content in the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var separatorLayoutGuide: UILayoutGuide { get }
```

#### Discussion

This property only takes effect in a layout section that supports separators, like a section that you create using [`list(using:layoutEnvironment:)`](nscollectionlayoutsection/list(using:layoutenvironment:).md).

The separator layout guide represents the frame of the separator, which the system uses to determine where to draw the separator at the bottom of the cell.

By default, when you apply a system-provided content configuration to a list cell, the separator automatically aligns to the primary text in the content view. For custom subviews in the cell, you need to add a constraint to this layout guide that connects it to the leading edge of the cell’s primary content.

![Diagram of a Favorites menu item with a separator below the cell, indicating another cell below. The separator layout guide appears around the frame of the separator. The leading edge of the separator layout guide is constrained to the leading edge of the primary content, the beginning of the word “Favorites.”](https://docs-assets.developer.apple.com/published/8604949838a7f6bcc3cba5d4bc284a2f/media-3680734%402x.png)

To align the separators to your content, add constraints to the leading or trailing anchors of this layout guide.

## See Also

- [var indentationLevel: Int](uicollectionviewlistcell/indentationlevel.md)
  The level of indentation for the cell.
- [var indentationWidth: CGFloat](uicollectionviewlistcell/indentationwidth.md)
  The width of an indentation level.
- [var indentsAccessories: Bool](uicollectionviewlistcell/indentsaccessories.md)
  A Boolean value that detemines whether the cell indents accessories on the leading side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/separatorlayoutguide)*