# headerImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An optional image to display in the header.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var headerImageProvider: CLKImageProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKImageProvider * headerImageProvider;
```

## Discussion

A tint color is applied to the header image to differentiate it from the other rows. In multicolor environments, the image provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
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
- [var column2Alignment: CLKComplicationColumnAlignment](./column2alignment.md)
  The alignment of the text in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable/headerimageprovider)*