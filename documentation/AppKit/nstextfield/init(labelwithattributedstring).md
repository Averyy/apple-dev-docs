# init(labelWithAttributedString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a text field for use as a static label that displays styled text, doesn’t wrap, and doesn’t have selectable text.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(labelWithAttributedString attributedStringValue: NSAttributedString)
```

```objc
+ (instancetype) labelWithAttributedString:(NSAttributedString *) attributedStringValue;
```

## Return Value

A text field that displays the specified attributed string as a static label.

## Discussion

The text field determines its line-break mode by inspecting the paragraph style attributes in the attributed string.

> **Note**:  When the text field has an attributed string value, the system ignores the [`textColor`](./textcolor.md), [`font`](../nscontrol/font.md), [`alignment`](../nscontrol/alignment.md), [`lineBreakMode`](../nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](../../Foundation/nsattributedstring/key/foregroundcolor.md), [`font`](../../Foundation/nsattributedstring/key/font.md), [`alignment`](../nsmutableparagraphstyle/alignment.md), linebreakmode, and [`lineBreakStrategy`](../nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## Parameters

- `attributedStringValue`: An attributed string to use as the content of the label.

## See Also

### Creating text fields
- [convenience init(labelWithString: String)](./init%28labelwithstring%29.md)
  Initializes a text field for use as a static label that uses the system default font, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(string: String)](./init%28string%29.md)
  Initializes a single-line editable text field for user input using the system default font and standard visual appearance.
- [convenience init(wrappingLabelWithString: String)](./init%28wrappinglabelwithstring%29.md)
  Initializes a text field for use as a multiline static label with selectable text that uses the system default font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/init(labelwithattributedstring:))*