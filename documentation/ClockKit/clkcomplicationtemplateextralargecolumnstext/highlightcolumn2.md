# highlightColumn2

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating which column should be drawn with a highlight.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var highlightColumn2: Bool { get set }
```

```objc
@property (nonatomic) BOOL highlightColumn2;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), text in column two is rendered with a highlight. When the value is [`false`](../../Swift/false.md), the text in column one is rendered with a highlight. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Setting the Complication Data
- [var column2Alignment: CLKComplicationColumnAlignment](./column2alignment.md)
  The alignment of the text in the second column.
- [var row1Column1TextProvider: CLKTextProvider](./row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](./row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](./row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](./row2column2textprovider.md)
  The text to display in the second column of the second row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargecolumnstext/highlightcolumn2)*