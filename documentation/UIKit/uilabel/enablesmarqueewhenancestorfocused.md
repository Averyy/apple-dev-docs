# enablesMarqueeWhenAncestorFocused

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var enablesMarqueeWhenAncestorFocused: Bool { get set }
```

```objc
@property (nonatomic) BOOL enablesMarqueeWhenAncestorFocused;
```

## Discussion

If this value is [`true`](../../Swift/true.md), then the label ignores [`lineBreakMode`](./linebreakmode.md), [`adjustsFontSizeToFitWidth`](./adjustsfontsizetofitwidth.md), and [`allowsDefaultTighteningForTruncation`](./allowsdefaulttighteningfortruncation.md). The label scrolls its text when any ancestor in its view hierarchy has focus.

The default value for this property is [`false`](../../Swift/false.md).

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
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var showsExpansionTextWhenTruncated: Bool](./showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/enablesmarqueewhenancestorfocused)*