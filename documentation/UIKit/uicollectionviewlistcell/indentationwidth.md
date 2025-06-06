# indentationWidth

**Framework**: UIKit  
**Kind**: property

The width of an indentation level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indentationWidth: CGFloat { get set }
```

#### Discussion

The overall indentation is the product of [`indentationWidth`](uicollectionviewlistcell/indentationwidth.md) and [`indentationLevel`](uicollectionviewlistcell/indentationlevel.md).

## See Also

- [var indentationLevel: Int](uicollectionviewlistcell/indentationlevel.md)
  The level of indentation for the cell.
- [var indentsAccessories: Bool](uicollectionviewlistcell/indentsaccessories.md)
  A Boolean value that detemines whether the cell indents accessories on the leading side.
- [var separatorLayoutGuide: UILayoutGuide](uicollectionviewlistcell/separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentationwidth)*