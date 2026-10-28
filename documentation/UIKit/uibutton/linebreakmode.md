# lineBreakMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The line break mode to use when drawing text.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the `lineBreakMode` property of the [`titleLabel`](./titlelabel.md) instead.

## Declaration

```objc
@property (nonatomic) NSLineBreakMode lineBreakMode;
```

## Discussion

This property is one of the constants described in the [`UILineBreakMode`](../uilinebreakmode.md) enumeration in NSString UIKit Additions Reference. The default value is [`UILineBreakModeMiddleTruncation`](../uilinebreakmode/uilinebreakmodemiddletruncation.md).

## See Also

### Deprecated title effects
- [font](./font.md)
  The font used to display text on the button.
- [titleShadowOffset](./titleshadowoffset.md)
  The offset of the shadow used to display the receiver’s title.
- [var reversesTitleShadowWhenHighlighted: Bool](./reversestitleshadowwhenhighlighted.md)
  A Boolean value that determines whether the title shadow changes when the button is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/linebreakmode)*