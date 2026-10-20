# font

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var font: UIFont! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) UIFont * font;
```

#### Discussion

If you’re using styled text, assigning a new value to this property applies the font to the entirety of the string in the [`attributedText`](./attributedtext.md) property. If you want to apply the font to only a portion of the text, create a new attributed string with the desired style information and associate it with the label. If you aren’t using styled text, this property applies to the entire text string in the [`text`](./text.md) property.

The default value for this property is the system font at a size of 17 points (using the [`systemFont(ofSize:)`](../uifont/systemfont%28ofsize%29.md) class method of [`UIFont`](../uifont.md)). Setting this property to `nil` causes it to be reset to the default value.

## See Also

### Accessing the text attributes
- [var text: String?](./text.md)
  The text that the label displays.
- [var attributedText: NSAttributedString?](./attributedtext.md)
  The styled text that the label displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/font)*