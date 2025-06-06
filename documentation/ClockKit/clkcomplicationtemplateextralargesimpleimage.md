# CLKComplicationTemplateExtraLargeSimpleImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeSimpleImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large image complication. The diagram show a single, large image.](https://docs-assets.developer.apple.com/published/32b8a6b1fe4603a06808cb7038555c94/media-2880769%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 182 pixels | 182 pixels |
| 40 mm | 203 pixels | 203 pixels |
| 41 mm | 215 pixels | 215 pixels |
| 42 mm | 203 pixels | 203 pixels |
| 44 mm | 224 pixels | 224 pixels |
| 45 mm | 242 pixels | 242 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider)](clkcomplicationtemplateextralargesimpleimage/init(imageprovider:).md)
  Creates a new template from the provided image.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplateextralargesimpleimage/imageprovider.md)
  The image to display in the complication.

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
- [class CLKComplicationTemplateExtraLargeStackImage](clkcomplicationtemplateextralargestackimage.md)
  A template for displaying a single image with a short line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpleimage)*