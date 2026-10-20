# textColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the text field’s content.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var textColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * textColor;
```

#### Discussion

> **Note**:  When the text field has an attributed string value, the system ignores the [`textColor`](./textcolor.md), [`font`](../nscontrol/font.md), [`alignment`](../nscontrol/alignment.md), [`lineBreakMode`](../nscontrol/linebreakmode.md), and `lineBreakStrategy` properties. Set the [`foregroundColor`](../../Foundation/nsattributedstring/key/foregroundcolor.md), [`font`](../../Foundation/nsattributedstring/key/font.md), [`alignment`](../nsmutableparagraphstyle/alignment.md), [`lineBreakMode`](../nsparagraphstyle/linebreakmode.md), and [`lineBreakStrategy`](../nsparagraphstyle/linebreakstrategy-swift.property.md) properties in the attributed string instead.

## See Also

### Related Documentation
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var textColor: NSColor?](../nstextfieldcell/textcolor.md)
  The color to use to draw the cell’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textcolor)*