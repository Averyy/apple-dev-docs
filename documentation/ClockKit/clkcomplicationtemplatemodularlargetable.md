# CLKComplicationTemplateModularLargeTable

**Framework**: ClockKit  
**Kind**: class

A template for displaying a header row and columns.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularLargeTable
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large table complication. The diagram shows a table with a header row and two rows of text, each containing two collumns. The table can also have an optional header image.](https://docs-assets.developer.apple.com/published/67e335fe5d5b361f5d28fdbd1286e265/media-2933750%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of the image must be between the specified minimum and maximum (inclusive).

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
- [init(headerTextProvider: CLKTextProvider, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargetable/init(headertextprovider:row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:).md)
  Creates a template that has a header and two columns of text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargetable/init(headerimageprovider:headertextprovider:row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:).md)
  Creates a template that has a header row with an image and text, and two columns of text.
### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargetable/headerimageprovider.md)
  An optional image to display in the header.
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

- [class CLKComplicationTemplateModularLargeColumns](clkcomplicationtemplatemodularlargecolumns.md)
  A template for displaying multiple columns of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable)*