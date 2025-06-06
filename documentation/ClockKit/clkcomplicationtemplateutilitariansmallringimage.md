# CLKComplicationTemplateUtilitarianSmallRingImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image encircled by a configurable progress ring

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallRingImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small ring image complication. The diagram shows an image inside a small progress ring.](https://docs-assets.developer.apple.com/published/095b83cc4e0d8681ec0e301bb73257e5/media-2933760%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 28 pixels | 28 pixels |
| 40 mm | 28 pixels | 28 pixels |
| 41 mm | 30  pixels | 30 pixels |
| 42 mm | 28 pixels | 28 pixels |
| 44 mm | 32 pixels | 32 pixels |
| 45 mm | 33 pixels | 33 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplateutilitariansmallringimage/init(imageprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplateutilitariansmallringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplateutilitariansmallringimage/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplateutilitariansmallringimage/fillfraction.md)
  The fraction of the ring to fill.

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

- [class CLKComplicationTemplateUtilitarianSmallFlat](clkcomplicationtemplateutilitariansmallflat.md)
  A template for displaying an image and text in a single line.
- [class CLKComplicationTemplateUtilitarianSmallRingText](clkcomplicationtemplateutilitariansmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateUtilitarianSmallSquare](clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringimage)*