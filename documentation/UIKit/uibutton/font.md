# font

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font used to display text on the button.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the `font` property of the [`titleLabel`](./titlelabel.md) instead.

## Declaration

```objc
@property (nonatomic, strong) UIFont * font;
```

#### Discussion

If `nil`, a system font is used. The default value is `nil`.

## See Also

### Related Documentation
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
### Deprecated title effects
- [lineBreakMode](./linebreakmode.md)
  The line break mode to use when drawing text.
- [titleShadowOffset](./titleshadowoffset.md)
  The offset of the shadow used to display the receiver’s title.
- [var reversesTitleShadowWhenHighlighted: Bool](./reversestitleshadowwhenhighlighted.md)
  A Boolean value that determines whether the title shadow changes when the button is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/font)*