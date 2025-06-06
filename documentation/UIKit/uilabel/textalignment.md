# textAlignment

**Framework**: UIKit  
**Kind**: property

The technique for aligning the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textAlignment: NSTextAlignment { get set }
```

#### Discussion

If you’re using styled text, assigning a new value to this property applies the text alignment to the entirety of the string in the [`attributedText`](uilabel/attributedtext.md) property. If you want to apply the alignment to only a portion of the text, create a new attributed string with the desired style information and associate it with the label. If you aren’t using styled text, this property applies to the entire text string in the [`text`](uilabel/text.md) property.

In iOS 9 and later, the default value of this property is [`NSTextAlignment.natural`](nstextalignment/natural.md); prior to iOS 9, the default value was [`NSTextAlignment.left`](nstextalignment/left.md).

## See Also

- [var text: String?](uilabel/text.md)
  The text that the label displays.
- [var attributedText: NSAttributedString?](uilabel/attributedtext.md)
  The styled text that the label displays.
- [var font: UIFont!](uilabel/font.md)
  The font of the text.
- [var textColor: UIColor!](uilabel/textcolor.md)
  The color of the text.
- [var lineBreakMode: NSLineBreakMode](uilabel/linebreakmode.md)
  The technique for wrapping and truncating the label’s text.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](uilabel/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var isEnabled: Bool](uilabel/isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/textalignment)*