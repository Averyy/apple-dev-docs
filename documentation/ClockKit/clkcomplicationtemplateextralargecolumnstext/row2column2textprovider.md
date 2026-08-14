# row2Column2TextProvider

**Framework**: ClockKit  
**Kind**: property

The text to display in the second column of the second row.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var row2Column2TextProvider: CLKTextProvider { get set }
```

#### Discussion

When the [`highlightColumn2`](clkcomplicationtemplateextralargecolumnstext/highlightcolumn2.md) property is [`true`](https://developer.apple.com/documentation/swift/true), a tint color is applied to this text. In multicolor environments, the text provider or template provides the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var column2Alignment: CLKComplicationColumnAlignment](clkcomplicationtemplateextralargecolumnstext/column2alignment.md)
  The alignment of the text in the second column.
- [var highlightColumn2: Bool](clkcomplicationtemplateextralargecolumnstext/highlightcolumn2.md)
  A Boolean value indicating which column should be drawn with a highlight.
- [var row1Column1TextProvider: CLKTextProvider](clkcomplicationtemplateextralargecolumnstext/row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](clkcomplicationtemplateextralargecolumnstext/row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](clkcomplicationtemplateextralargecolumnstext/row2column1textprovider.md)
  The text to display in the first column of the second row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/row2column2textprovider)*