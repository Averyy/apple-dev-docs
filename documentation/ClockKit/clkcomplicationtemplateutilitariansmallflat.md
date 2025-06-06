# CLKComplicationTemplateUtilitarianSmallFlat

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image and text in a single line.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallFlat
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small flat complication. The diagram shows a single row containing an image and a small amount of text.](https://docs-assets.developer.apple.com/published/415ed154130fdc7810590021060f7ab3/media-2933759%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of the image must be between the specified minimum and maximum (inclusive).

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 18 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 42 pixels maximum | 18 pixels |
| 40 mm | 20 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 44 pixels maximum | 20 pixels |
| 41 mm | 21 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 47 pixels maximum | 21 pixels |
| 42 mm | 20 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 44 pixels maximum | 20 pixels |
| 44 mm | 22 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 49 pixels maximum | 22 pixels |
| 45 mm | 24 pixels minimum ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 52 pixels maximum | 24 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider)](clkcomplicationtemplateutilitariansmallflat/init(textprovider:).md)
  Creates a new template that has a single line of text.
- [init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)](clkcomplicationtemplateutilitariansmallflat/init(textprovider:imageprovider:).md)
  Creates a new template that has a single row with an image and a line of text.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider?](clkcomplicationtemplateutilitariansmallflat/imageprovider.md)
  The image to display.
- [var textProvider: CLKTextProvider](clkcomplicationtemplateutilitariansmallflat/textprovider.md)
  The text to display.

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

- [class CLKComplicationTemplateUtilitarianSmallRingImage](clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallRingText](clkcomplicationtemplateutilitariansmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateUtilitarianSmallSquare](clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallflat)*