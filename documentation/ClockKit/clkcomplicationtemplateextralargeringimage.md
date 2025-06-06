# CLKComplicationTemplateExtraLargeRingImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image encircled by a configurable progress ring.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeRingImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large ring image complication. The diagram shows an image inside a progress ring.](https://docs-assets.developer.apple.com/published/58c879353ae4dd5af93e87d23e6d0b24/media-2880718%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 126 pixels | 126 pixels |
| 40 mm | 133 pixels | 133 pixels |
| 41 mm | 141 pixels | 141 pixels |
| 42 mm | 133 pixels | 133 pixels |
| 44 mm | 146 pixels | 146 pixels |
| 45 mm | 158 pixels | 158 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplateextralargeringimage/init(imageprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var fillFraction: Float](clkcomplicationtemplateextralargeringimage/fillfraction.md)
  The fraction of the ring to fill.
- [var imageProvider: CLKImageProvider](clkcomplicationtemplateextralargeringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplateextralargeringimage/ringstyle.md)
  The style of the progress ring.

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

- [class CLKComplicationTemplateExtraLargeSimpleImage](clkcomplicationtemplateextralargesimpleimage.md)
  A template for displaying an image.
- [class CLKComplicationTemplateExtraLargeStackImage](clkcomplicationtemplateextralargestackimage.md)
  A template for displaying a single image with a short line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringimage)*