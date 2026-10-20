# indentationWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The width of an indentation level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var indentationWidth: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat indentationWidth;
```

#### Discussion

The overall indentation is the product of [`indentationWidth`](./indentationwidth.md) and [`indentationLevel`](./indentationlevel.md).

## See Also

### Customizing layout
- [var indentationLevel: Int](./indentationlevel.md)
  The level of indentation for the cell.
- [var indentsAccessories: Bool](./indentsaccessories.md)
  A Boolean value that detemines whether the cell indents accessories on the leading side.
- [var separatorLayoutGuide: UILayoutGuide](./separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentationwidth)*