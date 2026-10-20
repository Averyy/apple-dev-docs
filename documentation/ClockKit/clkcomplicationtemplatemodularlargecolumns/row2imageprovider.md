# row2ImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An optional image to display at the beginning of the second row.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var row2ImageProvider: CLKImageProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKImageProvider * row2ImageProvider;
```

## See Also

### Setting the Complication Data
- [var row1ImageProvider: CLKImageProvider?](./row1imageprovider.md)
  An optional image to display at the beginning of the first row.
- [var row1Column1TextProvider: CLKTextProvider](./row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](./row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2Column1TextProvider: CLKTextProvider](./row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](./row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var row3ImageProvider: CLKImageProvider?](./row3imageprovider.md)
  An optional image to display at the beginning of the third row.
- [var row3Column1TextProvider: CLKTextProvider](./row3column1textprovider.md)
  The text to display in the first column of the third row.
- [var row3Column2TextProvider: CLKTextProvider](./row3column2textprovider.md)
  The text to display in the second column of the third row.
- [var column2Alignment: CLKComplicationColumnAlignment](./column2alignment.md)
  The alignment of the text in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargecolumns/row2imageprovider)*