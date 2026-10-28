# CLKComplicationTemplateModularSmallRingImage

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying an image encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularSmallRingImage
```

```objc
@interface CLKComplicationTemplateModularSmallRingImage : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](./clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small ring image complication. The diagram shows an image inside a small progress ring.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933751@2x.png)

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
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./clkcomplicationtemplatemodularsmallringimage/init%28imageprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided image, fill fraction, and ring style.
- [+ templateWithImageProvider:fillFraction:ringStyle:](./clkcomplicationtemplatemodularsmallringimage/templatewithimageprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](./clkcomplicationtemplatemodularsmallringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](./clkcomplicationtemplatemodularsmallringimage/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](./clkcomplicationtemplatemodularsmallringimage/fillfraction.md)
  The fraction of the ring to fill.

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

### Image templates
- [class CLKComplicationTemplateModularSmallSimpleImage](./clkcomplicationtemplatemodularsmallsimpleimage.md)
  A template for displaying an image.
- [class CLKComplicationTemplateModularSmallStackImage](./clkcomplicationtemplatemodularsmallstackimage.md)
  A template for displaying a single image with a short line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringimage)*