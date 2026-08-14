# CLKComplicationTemplateUtilitarianLargeFlat

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image and string in a single long line.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateUtilitarianLargeFlat
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianLarge`](clkcomplicationfamily/utilitarianlarge.md) family.

![Diagram showing the layout of a row containing an image and text.](/images/com.apple.clockkit/media-2933763@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of each image must be between the specified minimum and maximum (inclusive).

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 18 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 42 pixels maximum | 18 pixels |
| 40 mm | 20 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 44 pixels maximum | 20 pixels |
| 41 mm | 21 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 47 pixels maximum | 21 pixels |
| 42 mm | 20 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 44 pixels maximum | 20 pixels |
| 44 mm | 22 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 49 pixels maximum | 22 pixels |
| 45 mm | 24 pixels minimum ![None](/images/com.apple.clockkit/spacer.png) 52 pixels maximum | 24 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider)](clkcomplicationtemplateutilitarianlargeflat/init(textprovider:).md)
  Creates a new template that has a long line of text.
- [init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)](clkcomplicationtemplateutilitarianlargeflat/init(textprovider:imageprovider:).md)
  Creates a new template that has a single row with an image and a long line of text.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](clkcomplicationtemplateutilitarianlargeflat/textprovider.md)
  The text to display.
- [var imageProvider: CLKImageProvider?](clkcomplicationtemplateutilitarianlargeflat/imageprovider.md)
  The image to display.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitarianlargeflat)*