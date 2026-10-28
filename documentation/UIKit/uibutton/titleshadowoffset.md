# titleShadowOffset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The offset of the shadow used to display the receiver’s title.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the `shadowOffset` property of the [`titleLabel`](./titlelabel.md) instead.

## Declaration

```objc
@property (nonatomic) CGSize titleShadowOffset;
```

## Discussion

The horizontal and vertical offset values, specified using the `width` and `height` fields of the `CGSize` data type. Positive values always extend up and to the right from the user’s perspective. The default value is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md).

## See Also

### Related Documentation
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
### Deprecated title effects
- [font](./font.md)
  The font used to display text on the button.
- [lineBreakMode](./linebreakmode.md)
  The line break mode to use when drawing text.
- [var reversesTitleShadowWhenHighlighted: Bool](./reversestitleshadowwhenhighlighted.md)
  A Boolean value that determines whether the title shadow changes when the button is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/titleshadowoffset)*