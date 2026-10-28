# column2Alignment

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the text in the second column.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var column2Alignment: CLKComplicationColumnAlignment { get set }
```

```objc
@property (nonatomic) CLKComplicationColumnAlignment column2Alignment;
```

## Discussion

This alignment value applies to the text in column two of both rows. It doesn’t apply to the text in the header line.

## See Also

### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](./headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The text to display in the header line.
- [var row1Column1TextProvider: CLKTextProvider](./row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](./row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](./row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](./row2column2textprovider.md)
  The text to display in the second column of the second row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable/column2alignment)*