# CLKComplicationTemplateModularSmallColumnsText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two rows and two columns of text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularSmallColumnsText
```

```objc
@interface CLKComplicationTemplateModularSmallColumnsText : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](./clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small columns text complication. The diagram shows two rows, each with two columns of text. ](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933754@2x.png)

## Topics

### Creating the Template
- [init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularsmallcolumnstext/init%28row1column1textprovider,row1column2textprovider,row2column1textprovider,row2column2textprovider%29.md)
  Creates a new template that has two columns of text.
- [+ templateWithRow1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:](./clkcomplicationtemplatemodularsmallcolumnstext/templatewithrow1column1textprovider_row1column2textprovider_row2column1textprovider_row2column2textprovider_.md)
  Returns a new template that has two columns of text.
### Setting the Complication Data
- [var row1Column1TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallcolumnstext/row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallcolumnstext/row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallcolumnstext/row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallcolumnstext/row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var column2Alignment: CLKComplicationColumnAlignment](./clkcomplicationtemplatemodularsmallcolumnstext/column2alignment.md)
  The alignment of the text in the second column.
- [var highlightColumn2: Bool](./clkcomplicationtemplatemodularsmallcolumnstext/highlightcolumn2.md)
  A Boolean value indicating which column should be drawn with a highlight.

## Relationships

### Inherits From
- [CLKComplicationTemplate](./clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text templates
- [class CLKComplicationTemplateModularSmallRingText](./clkcomplicationtemplatemodularsmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallSimpleText](./clkcomplicationtemplatemodularsmallsimpletext.md)
  A template for displaying a small amount of text.
- [class CLKComplicationTemplateModularSmallStackText](./clkcomplicationtemplatemodularsmallstacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallcolumnstext)*