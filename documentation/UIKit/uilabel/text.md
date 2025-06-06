# text

**Framework**: UIKit  
**Kind**: property

The text that the label displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var text: String? { get set }
```

#### Discussion

This property is `nil` by default. Assigning a new value to this property also replaces the value of the [`attributedText`](uilabel/attributedtext.md) property with the same text, although without any inherent style attributes. Instead the label styles the new string using [`shadowColor`](uilabel/shadowcolor.md), [`textAlignment`](uilabel/textalignment.md), and other style-related properties of the class.

## See Also

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
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](uilabel/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/text)*