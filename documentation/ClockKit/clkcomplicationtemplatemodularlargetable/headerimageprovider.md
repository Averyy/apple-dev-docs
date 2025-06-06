# headerImageProvider

**Framework**: ClockKit  
**Kind**: property

An optional image to display in the header.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var headerImageProvider: CLKImageProvider? { get set }
```

#### Discussion

A tint color is applied to the header image to differentiate it from the other rows. In multicolor environments, the image provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetable/headertextprovider.md)
  The text to display in the header line.
- [var row1Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetable/row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetable/row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetable/row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetable/row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var column2Alignment: CLKComplicationColumnAlignment](clkcomplicationtemplatemodularlargetable/column2alignment.md)
  The alignment of the text in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable/headerimageprovider)*