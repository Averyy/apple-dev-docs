# showsExpansionTextWhenTruncated

**Framework**: Uikit  
**Kind**: property

A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsExpansionTextWhenTruncated: Bool { get set }
```

#### Discussion

A label may truncate text too long to fit in its container based on the value of the label’s [`lineBreakMode`](uilabel/linebreakmode.md) property. To provide the option in your app to show the full text when the pointer hovers over the truncated text, set [`showsExpansionTextWhenTruncated`](uilabel/showsexpansiontextwhentruncated.md) to [`true`](https://developer.apple.com/documentation/swift/true). The default value is [`false`](https://developer.apple.com/documentation/swift/false).

![An illustration showing three views extending horizontally. Each view displays an icon on the left, followed by title and subtitle labels on the right side of the view. The title appears above the subtitle. A line with an arrow at the end extends from the first view to the second view, and from the second view to the third view. The first view shows an arrow pointer positioned outside of the view. The second view shows the pointer positioned over truncated text in the subtitle label. The third view shows the expanded text as the pointer continues to hover over the subtitle label.](https://docs-assets.developer.apple.com/published/be842db59029dc8187d04688ca5acc58/media-3875433%402x.png)

> **Note**:  Text expansion is available in iPhone and iPad apps running on a Mac with Apple silicon and in Mac apps built with [`Mac Catalyst`](mac-catalyst.md).

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
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/showsexpansiontextwhentruncated)*