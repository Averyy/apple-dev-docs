# CLKComplicationTemplateUtilitarianSmallFlat

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying an image and text in a single line.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallFlat
```

```objc
@interface CLKComplicationTemplateUtilitarianSmallFlat : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](./clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small flat complication. The diagram shows a single row containing an image and a small amount of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933759@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of the image must be between the specified minimum and maximum (inclusive).

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 18 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 42 pixels maximum | 18 pixels |
| 40 mm | 20 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 44 pixels maximum | 20 pixels |
| 41 mm | 21 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 47 pixels maximum | 21 pixels |
| 42 mm | 20 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 44 pixels maximum | 20 pixels |
| 44 mm | 22 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 49 pixels maximum | 22 pixels |
| 45 mm | 24 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 52 pixels maximum | 24 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider)](./clkcomplicationtemplateutilitariansmallflat/init%28textprovider%29.md)
  Creates a new template that has a single line of text.
- [init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)](./clkcomplicationtemplateutilitariansmallflat/init%28textprovider,imageprovider%29.md)
  Creates a new template that has a single row with an image and a line of text.
- [+ templateWithTextProvider:](./clkcomplicationtemplateutilitariansmallflat/templatewithtextprovider_.md)
  Returns a new template that has a single line of text.
- [+ templateWithTextProvider:imageProvider:](./clkcomplicationtemplateutilitariansmallflat/templatewithtextprovider_imageprovider_.md)
  Returns a new template that has a single row with an image and a line of text.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider?](./clkcomplicationtemplateutilitariansmallflat/imageprovider.md)
  The image to display.
- [var textProvider: CLKTextProvider](./clkcomplicationtemplateutilitariansmallflat/textprovider.md)
  The text to display.

## Relationships

### Inherits From
- [CLKComplicationTemplate](./clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Utilitarian small
- [class CLKComplicationTemplateUtilitarianSmallRingImage](./clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallRingText](./clkcomplicationtemplateutilitariansmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateUtilitarianSmallSquare](./clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallflat)*