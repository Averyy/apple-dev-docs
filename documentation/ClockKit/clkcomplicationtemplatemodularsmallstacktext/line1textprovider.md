# line1TextProvider

**Framework**: ClockKit  
**Kind**: property

The text to display on the top line of the complication.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var line1TextProvider: CLKTextProvider { get set }
```

#### Discussion

Space for text is limited in this particular template so keep strings as short as possible.

When the [`highlightLine2`](clkcomplicationtemplatemodularsmallstacktext/highlightline2.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), a tint color is applied to this text. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallstacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.
- [var highlightLine2: Bool](clkcomplicationtemplatemodularsmallstacktext/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstacktext/line1textprovider)*