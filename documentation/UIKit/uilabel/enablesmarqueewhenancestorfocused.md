# enablesMarqueeWhenAncestorFocused

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var enablesMarqueeWhenAncestorFocused: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/Swift/true), then the label ignores [`lineBreakMode`](uilabel/linebreakmode.md), [`adjustsFontSizeToFitWidth`](uilabel/adjustsfontsizetofitwidth.md), and [`allowsDefaultTighteningForTruncation`](uilabel/allowsdefaulttighteningfortruncation.md). The label scrolls its text when any ancestor in its view hierarchy has focus.

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var text: String?](uilabel/text.md)
  The text that the label displays.
- [var attributedText: NSAttributedString?](uilabel/attributedtext.md)
  The styled text that the label displays.
- [var font: UIFont!](uilabel/font.md)
  The font of the text.
- [var textColor: UIColor!](uilabel/textcolor.md)
  The color of the text.
- [var textAlignment: NSTextAlignment](uilabel/textalignment.md)
  The technique for aligning the text.
- [var lineBreakMode: NSLineBreakMode](uilabel/linebreakmode.md)
  The technique for wrapping and truncating the label’s text.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](uilabel/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var isEnabled: Bool](uilabel/isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/enablesmarqueewhenancestorfocused)*