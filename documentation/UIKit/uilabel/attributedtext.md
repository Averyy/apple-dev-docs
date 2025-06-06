# attributedText

**Framework**: UIKit  
**Kind**: property

The styled text that the label displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var attributedText: NSAttributedString? { get set }
```

#### Discussion

This property is `nil` by default.

Assigning a new value to this property also replaces the value of the [`text`](uilabel/text.md) property with the same string data, although without any formatting information. In addition, assigning a new value updates the values in the [`font`](uilabel/font.md), [`textColor`](uilabel/textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

Turn autokerning on for the label by setting the [`kern`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1527891-kern) (Swift) or [`NSKernAttributeName`](nskernattributename.md) (Objective-C) of the string to doc://com.apple.documentation/documentation/foundation/nsnull/1520557-null.

## See Also

- [var text: String?](uilabel/text.md)
  The text that the label displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/attributedtext)*