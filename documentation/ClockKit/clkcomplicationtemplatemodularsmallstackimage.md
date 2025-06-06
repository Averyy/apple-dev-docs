# CLKComplicationTemplateModularSmallStackImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a single image with a short line of text below it.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularSmallStackImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](clkcomplicationfamily/modularsmall.md) family.

![Diagram showing the layout of a small image positioned above a short line of text.](https://docs-assets.developer.apple.com/published/967c65a22885263538ee4fdeb7e859d2/media-2933753%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 52 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 28 pixels |
| 40 mm | 58 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 30 pixels |
| 41 mm | 61 pixels ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 32 pixels |
| 42 mm | 58 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 30 pixels |
| 44 mm | 64 pixels maximum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 34 pixels |
| 45 mm | 69 pixels ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (You may specify images with a smaller width.) | 36 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(line1ImageProvider: CLKImageProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularsmallstackimage/init(line1imageprovider:line2textprovider:).md)
  Creates a new template from the provided image and text.
### Setting the Complication Data
- [var line1ImageProvider: CLKImageProvider](clkcomplicationtemplatemodularsmallstackimage/line1imageprovider.md)
  The image to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallstackimage/line2textprovider.md)
  The text to display on the bottom line of the complication.
- [var highlightLine2: Bool](clkcomplicationtemplatemodularsmallstackimage/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.

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

- [class CLKComplicationTemplateModularSmallRingImage](clkcomplicationtemplatemodularsmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallSimpleImage](clkcomplicationtemplatemodularsmallsimpleimage.md)
  A template for displaying an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstackimage)*