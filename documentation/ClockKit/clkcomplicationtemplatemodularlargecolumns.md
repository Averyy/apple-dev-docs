# CLKComplicationTemplateModularLargeColumns

**Framework**: ClockKit  
**Kind**: class

A template for displaying multiple columns of data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularLargeColumns
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large columns complication. The diagram shows two columns with three rows of text and an optional column of images.](https://docs-assets.developer.apple.com/published/1dbabdd88e9966549fbe4d839e5ff002/media-2933749%402x.png)

The following table lists the dimensions of the images you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of each image must be between the specified minimum and maximum (inclusive).

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 22 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 64 pixels maximum | 22 pixels |
| 40 mm | 24 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 74 pixels maximum | 24 pixels |
| 41 mm | 25 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 78 pixels maximum | 25 pixels |
| 42 mm | 24 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 74 pixels maximum | 24 pixels |
| 44 mm | 28 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 84 pixels maximum | 28 pixels |
| 45 mm | 29 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 88 pixels maximum | 29 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargecolumns/init(row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:row3column1textprovider:row3column2textprovider:).md)
  Creates a template that has two columns of text.
- [init(row1ImageProvider: CLKImageProvider?, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2ImageProvider: CLKImageProvider?, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3ImageProvider: CLKImageProvider?, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargecolumns/init(row1imageprovider:row1column1textprovider:row1column2textprovider:row2imageprovider:row2column1textprovider:row2column2textprovider:row3imageprovider:row3column1textprovider:row3column2textprovider:).md)
  Creates a template that has a column of images and two columns of text.
### Setting the Complication Data
- [var row1ImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargecolumns/row1imageprovider.md)
  An optional image to display at the beginning of the first row.
- [var row1Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row1column1textprovider.md)
  The text to display in the first column of the first row.
- [var row1Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row1column2textprovider.md)
  The text to display in the second column of the first row.
- [var row2ImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargecolumns/row2imageprovider.md)
  An optional image to display at the beginning of the second row.
- [var row2Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row2column1textprovider.md)
  The text to display in the first column of the second row.
- [var row2Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row2column2textprovider.md)
  The text to display in the second column of the second row.
- [var row3ImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargecolumns/row3imageprovider.md)
  An optional image to display at the beginning of the third row.
- [var row3Column1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row3column1textprovider.md)
  The text to display in the first column of the third row.
- [var row3Column2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargecolumns/row3column2textprovider.md)
  The text to display in the second column of the third row.
- [var column2Alignment: CLKComplicationColumnAlignment](clkcomplicationtemplatemodularlargecolumns/column2alignment.md)
  The alignment of the text in the second column.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateModularLargeTable](clkcomplicationtemplatemodularlargetable.md)
  A template for displaying a header row and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargecolumns)*