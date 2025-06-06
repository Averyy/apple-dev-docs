# CLKComplicationTemplateExtraLargeStackImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a single image with a short line of text below it.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeStackImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large stack image complication. The diagram shows an image positioned above a short line of text.](https://docs-assets.developer.apple.com/published/26ec341b082dc58d671c01dad213be63/media-2880768%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 156 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 84 pixels |
| 40 mm | 174 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 90 pixels |
| 41 mm | 192 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 95 pixels |
| 42 mm | 174 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 90 pixels |
| 44 mm | 192 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 102 pixels |
| 45 mm | 207 pixels ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 107 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(line1ImageProvider: CLKImageProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplateextralargestackimage/init(line1imageprovider:line2textprovider:).md)
  Creates a new template from the provided image and text.
### Setting the Complication Data
- [var highlightLine2: Bool](clkcomplicationtemplateextralargestackimage/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.
- [var line1ImageProvider: CLKImageProvider](clkcomplicationtemplateextralargestackimage/line1imageprovider.md)
  The image to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplateextralargestackimage/line2textprovider.md)
  The text to display on the bottom line of the complication.

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

- [class CLKComplicationTemplateExtraLargeRingImage](clkcomplicationtemplateextralargeringimage.md)
  A template for displaying an image encircled by a configurable progress ring.
- [class CLKComplicationTemplateExtraLargeSimpleImage](clkcomplicationtemplateextralargesimpleimage.md)
  A template for displaying an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage)*