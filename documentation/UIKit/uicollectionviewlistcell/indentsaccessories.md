# indentsAccessories

**Framework**: UIKit  
**Kind**: property

A Boolean value that detemines whether the cell indents accessories on the leading side.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indentsAccessories: Bool { get set }
```

#### Discussion

If the value is [`false`](https://developer.apple.com/documentation/Swift/false), the cell indents the content view only.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var indentationLevel: Int](uicollectionviewlistcell/indentationlevel.md)
  The level of indentation for the cell.
- [var indentationWidth: CGFloat](uicollectionviewlistcell/indentationwidth.md)
  The width of an indentation level.
- [var separatorLayoutGuide: UILayoutGuide](uicollectionviewlistcell/separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentsaccessories)*