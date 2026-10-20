# lineBreakStrategy

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The strategy that the system uses to break lines when laying out multiple lines of text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

```objc
@property (nonatomic) NSLineBreakStrategy lineBreakStrategy;
```

#### Discussion

The default value is [`standard`](../nsparagraphstyle/linebreakstrategy-swift.struct/standard.md).

> **Note**:  When the label has an attributed string value, the system ignores the [`textColor`](./textcolor.md), [`font`](./font.md), [`textAlignment`](./textalignment.md), [`lineBreakMode`](./linebreakmode.md), and [`lineBreakStrategy`](./linebreakstrategy.md) properties. Set the [`NSForegroundColorAttributeName`](../nsforegroundcolorattributename.md), [`NSFontAttributeName`](../nsfontattributename.md), [`alignment`](../nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](../nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](../nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

### Accessing the text attributes
- [var text: String?](./text.md)
  The text that the label displays.
- [var attributedText: NSAttributedString?](./attributedtext.md)
  The styled text that the label displays.
- [var font: UIFont!](./font.md)
  The font of the text.
- [var textColor: UIColor!](./textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The technique for aligning the text.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The technique for wrapping and truncating the label’s text.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var enablesMarqueeWhenAncestorFocused: Bool](./enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](./showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/linebreakstrategy)*