# indentsAccessories

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that detemines whether the cell indents accessories on the leading side.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var indentsAccessories: Bool { get set }
```

```objc
@property (nonatomic) BOOL indentsAccessories;
```

## Discussion

If the value is [`false`](../../Swift/false.md), the cell indents the content view only.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Customizing layout
- [var indentationLevel: Int](./indentationlevel.md)
  The level of indentation for the cell.
- [var indentationWidth: CGFloat](./indentationwidth.md)
  The width of an indentation level.
- [var separatorLayoutGuide: UILayoutGuide](./separatorlayoutguide.md)
  A guide for laying out separators in relation to the primary content in the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentsaccessories)*