# CLKComplicationTemplateModularSmallSimpleImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularSmallSimpleImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small simple image complication. The diagram shows a single, small image.](https://docs-assets.developer.apple.com/published/073d487a0daac572fa6ff050a764d473/media-2933752%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch size | Width | Height |
| --- | --- | --- |
| 38 mm | 52 pixels | 52 pixels |
| 40 mm | 58 pixels | 58 pixels |
| 41 mm | 61 pixels | 61 pixels |
| 42 mm | 58 pixels | 58 pixels |
| 44 mm | 64 pixels | 64 pixels |
| 45 mm | 69 pixels | 69 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider)](clkcomplicationtemplatemodularsmallsimpleimage/init(imageprovider:).md)
  Creates a new template from the provided image.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplatemodularsmallsimpleimage/imageprovider.md)
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

- [class CLKComplicationTemplateModularSmallRingImage](clkcomplicationtemplatemodularsmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallStackImage](clkcomplicationtemplatemodularsmallstackimage.md)
  A template for displaying a single image with a short line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallsimpleimage)*