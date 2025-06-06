# lineBreakStrategy

**Framework**: Uikit  
**Kind**: property

The strategy that the system uses to break lines when laying out multiple lines of text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy { get set }
```

#### Discussion

The default value is [`standard`](nsparagraphstyle/linebreakstrategy-swift.struct/standard.md).

> **Note**:  When the label has an attributed string value, the system ignores the [`textColor`](uilabel/textcolor.md), [`font`](uilabel/font.md), [`textAlignment`](uilabel/textalignment.md), [`lineBreakMode`](uilabel/linebreakmode.md), and [`lineBreakStrategy`](uilabel/linebreakstrategy.md) properties. Set the [`foregroundColor`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1533563-foregroundcolor) (Swift)/[`NSForegroundColorAttributeName`](nsforegroundcolorattributename.md) (Objective-C), [`font`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1528839-font) (Swift)/[`NSFontAttributeName`](nsfontattributename.md) (Objective-C), [`alignment`](nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

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
- [var isEnabled: Bool](uilabel/isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/linebreakstrategy)*