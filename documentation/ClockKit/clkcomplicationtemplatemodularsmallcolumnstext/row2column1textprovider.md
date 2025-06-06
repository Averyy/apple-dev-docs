# row2Column1TextProvider

**Framework**: ClockKit  
**Kind**: property

The text to display in the first column of the second row.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var row2Column1TextProvider: CLKTextProvider { get set }
```

#### Discussion

When the [`highlightColumn2`](clkcomplicationtemplatemodularsmallcolumnstext/highlightcolumn2.md) property is [`false`](https://developer.apple.com/documentation/swift/false), a tint color is applied to this text. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var row1Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallcolumnstext/row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallcolumnstext/row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallcolumnstext/row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var column2Alignment: CLKComplicationColumnAlignment](clkcomplicationtemplatemodularsmallcolumnstext/column2alignment.md)
  The alignment of the text in the second column.
- [var highlightColumn2: Bool](clkcomplicationtemplatemodularsmallcolumnstext/highlightcolumn2.md)
  A Boolean value indicating which column should be drawn with a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallcolumnstext/row2column1textprovider)*