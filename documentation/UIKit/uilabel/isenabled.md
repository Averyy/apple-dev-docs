# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the label draws its text in an enabled state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

This property determines only how the label draws its text. The label dims the text somewhat when not enabled to indicate it’s not active. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

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
- [var lineBreakMode: NSLineBreakMode](uilabel/linebreakmode.md)
  The technique for wrapping and truncating the label’s text.
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](uilabel/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/isenabled)*