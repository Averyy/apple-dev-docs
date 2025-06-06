# CLKComplicationTemplateCircularSmallRingImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a single image surrounded by a configurable progress ring.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateCircularSmallRingImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of a circular small image complication. The diagram shows three versions, each with an image inside a small progress ring.](https://docs-assets.developer.apple.com/published/b6d6cb1fec43fe7089e08e28034c789d/media-2933734%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 40 pixels | 40 pixels |
| 40 mm | 44 pixels | 44 pixels |
| 41 mm | 47 pixels | 47 pixels |
| 42 mm | 44 pixels | 44 pixels |
| 44 mm | 48 pixels | 48 pixels |
| 45 mm | 52 pixels | 52 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplatecircularsmallringimage/init(imageprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplatecircularsmallringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplatecircularsmallringimage/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplatecircularsmallringimage/fillfraction.md)
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

- [class CLKComplicationTemplateCircularSmallSimpleImage](clkcomplicationtemplatecircularsmallsimpleimage.md)
  A template for displaying a single image.
- [class CLKComplicationTemplateCircularSmallStackImage](clkcomplicationtemplatecircularsmallstackimage.md)
  A template for displaying an image with a line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringimage)*