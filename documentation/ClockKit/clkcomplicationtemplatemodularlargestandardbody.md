# CLKComplicationTemplateModularLargeStandardBody

**Framework**: ClockKit  
**Kind**: class

A template for displaying a header row and two lines of text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularLargeStandardBody
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large standard body complication. The diagram shows the header row, two lines of text, and an optional header image.](https://docs-assets.developer.apple.com/published/73935aa50a5db3e135d5a61cae9efb08/media-2933747%402x.png)

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
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:).md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:).md)
  Creates a new template that has a header row with an image and text, and a row of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a header row with an image and text, and two rows of body text.
### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargestandardbody/headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](clkcomplicationtemplatemodularlargestandardbody/body2textprovider.md)
  An optional second line of body text.

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

- [class CLKComplicationTemplateModularLargeTallBody](clkcomplicationtemplatemodularlargetallbody.md)
  A template for displaying a header row and row of tall body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody)*