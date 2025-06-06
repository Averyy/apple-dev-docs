# CLKComplicationTemplateModularSmallRingImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularSmallRingImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small ring image complication. The diagram shows an image inside a small progress ring.](https://docs-assets.developer.apple.com/published/cc28f9c6d3731f978b9a811873e1f6db/media-2933751%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 36 pixels | 36 pixels |
| 40 mm | 38 pixels | 38 pixels |
| 41 mm | 40 pixels | 40 pixels |
| 42 mm | 38 pixels | 38 pixels |
| 44 mm | 42 pixels | 42 pixels |
| 45 mm | 45 pixels | 45 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplatemodularsmallringimage/init(imageprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplatemodularsmallringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplatemodularsmallringimage/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplatemodularsmallringimage/fillfraction.md)
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

- [class CLKComplicationTemplateModularSmallSimpleImage](clkcomplicationtemplatemodularsmallsimpleimage.md)
  A template for displaying an image.
- [class CLKComplicationTemplateModularSmallStackImage](clkcomplicationtemplatemodularsmallstackimage.md)
  A template for displaying a single image with a short line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringimage)*