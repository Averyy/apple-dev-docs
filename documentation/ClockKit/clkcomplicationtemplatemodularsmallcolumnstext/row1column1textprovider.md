# row1Column1TextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the first column of the first row.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var row1Column1TextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * row1Column1TextProvider;
```

## Discussion

When the [`highlightColumn2`](./highlightcolumn2.md) property is [`false`](../../Swift/false.md), a tint color is applied to this text. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
- [var row1Column2TextProvider: CLKTextProvider](./row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](./row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](./row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var column2Alignment: CLKComplicationColumnAlignment](./column2alignment.md)
  The alignment of the text in the second column.
- [var highlightColumn2: Bool](./highlightcolumn2.md)
  A Boolean value indicating which column should be drawn with a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallcolumnstext/row1column1textprovider)*