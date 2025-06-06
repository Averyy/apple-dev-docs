# CLKComplicationTemplateUtilitarianSmallSquare

**Framework**: ClockKit  
**Kind**: class

A template for displaying a single square image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallSquare
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small square complication. The diagram shows a single, small image.](https://docs-assets.developer.apple.com/published/e58d4252d096df8edb14a236a324d7d3/media-2933762%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 40 pixels | 40 pixels |
| 40 mm | 44 pixels | 44 pixels |
| 41 mm | 47 pixels | 47 pixels |
| 42 mm | 44 pixels | 44 pixels |
| 44 mm | 50 pixels | 50 pixels |
| 45 mm | 52 pixels | 52 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKImageProvider)](clkcomplicationtemplateutilitariansmallsquare/init(imageprovider:).md)
  Creates a new template that has a square image.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](clkcomplicationtemplateutilitariansmallsquare/imageprovider.md)
  The image to display.

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
- [class CLKComplicationTemplateUtilitarianSmallRingImage](clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallRingText](clkcomplicationtemplateutilitariansmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallsquare)*