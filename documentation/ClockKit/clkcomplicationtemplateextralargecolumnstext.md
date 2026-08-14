# CLKComplicationTemplateExtraLargeColumnsText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two rows and two columns of text.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeColumnsText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large columns text complication. The diagram shows two rows, each containing two columns of text. ](/images/com.apple.clockkit/media-2919001@2x.png)

## Topics

### Creating the Template
- [init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](clkcomplicationtemplateextralargecolumnstext/init(row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:).md)
  Creates a new template that has two columns of text.
### Setting the Complication Data
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
- [var row2Column2TextProvider: CLKTextProvider](clkcomplicationtemplateextralargecolumnstext/row2column2textprovider.md)
  The text to display in the second column of the second row.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateExtraLargeRingText](clkcomplicationtemplateextralargeringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateExtraLargeSimpleText](clkcomplicationtemplateextralargesimpletext.md)
  A template for displaying a small amount of text.
- [class CLKComplicationTemplateExtraLargeStackText](clkcomplicationtemplateextralargestacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext)*