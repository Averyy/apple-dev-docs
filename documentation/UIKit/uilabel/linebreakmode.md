# lineBreakMode

**Framework**: UIKit  
**Kind**: property

The technique for wrapping and truncating the label’s text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var lineBreakMode: NSLineBreakMode { get set }
```

#### Discussion

If you aren’t using styled text, this property applies to the entire text string in the [`text`](uilabel/text.md) property. If you’re using styled text, assigning a new value to this property applies the line break mode to the entirety of the string in the [`attributedText`](uilabel/attributedtext.md) property. To apply the line break mode to only a portion of the text, create a new attributed string with the desired style information and associate it with the label. However, [`NSParagraphStyle`](nsparagraphstyle.md) properties, such as those defined by [`NSLineBreakMode`](nslinebreakmode.md), apply to entire paragraphs (as defined for [`paragraphRange(for:)`](https://developer.apple.com/documentation/foundation/nsstring/1408548-paragraphrange)), not words within paragraphs.

This property is in effect both during normal drawing and in cases where the label must reduce the font size to fit the text in its bounding box. The default value of this property is [`NSLineBreakMode.byTruncatingTail`](nslinebreakmode/bytruncatingtail.md).

## See Also

- [var adjustsFontSizeToFitWidth: Bool](uilabel/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
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
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](uilabel/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var isEnabled: Bool](uilabel/isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/linebreakmode)*