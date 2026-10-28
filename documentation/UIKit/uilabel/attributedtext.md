# attributedText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The styled text that the label displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedText: NSAttributedString? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedText;
```

## Discussion

This property is `nil` by default.

Assigning a new value to this property also replaces the value of the [`text`](./text.md) property with the same string data, although without any formatting information. In addition, assigning a new value updates the values in the [`font`](./font.md), [`textColor`](./textcolor.md), and other style-related properties so that they reflect the style information starting at location `0` in the attributed string.

Turn autokerning on for the label by setting the [`NSKernAttributeName`](../nskernattributename.md) of the string to [`null`](../../Foundation/nsnull/null.md).

## See Also

### Accessing the text attributes
- [var text: String?](./text.md)
  The text that the label displays.
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
- [var enablesMarqueeWhenAncestorFocused: Bool](./enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var showsExpansionTextWhenTruncated: Bool](./showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text of the label displays when the pointer hovers over the truncated text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/attributedtext)*