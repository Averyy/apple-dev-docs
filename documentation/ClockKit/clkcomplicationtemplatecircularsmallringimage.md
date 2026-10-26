# CLKComplicationTemplateCircularSmallRingImage

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a single image surrounded by a configurable progress ring.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateCircularSmallRingImage
```

```objc
@interface CLKComplicationTemplateCircularSmallRingImage : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](./clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of a circular small image complication. The diagram shows three versions, each with an image inside a small progress ring.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933734@2x.png)

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
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./clkcomplicationtemplatecircularsmallringimage/init%28imageprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided image, fill fraction, and ring style.
- [+ templateWithImageProvider:fillFraction:ringStyle:](./clkcomplicationtemplatecircularsmallringimage/templatewithimageprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided image, fill fraction, and ring style.
### Setting the Complication Data
- [var imageProvider: CLKImageProvider](./clkcomplicationtemplatecircularsmallringimage/imageprovider.md)
  The image to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](./clkcomplicationtemplatecircularsmallringimage/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](./clkcomplicationtemplatecircularsmallringimage/fillfraction.md)
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
- [class CLKComplicationTemplateCircularSmallSimpleImage](./clkcomplicationtemplatecircularsmallsimpleimage.md)
  A template for displaying a single image.
- [class CLKComplicationTemplateCircularSmallStackImage](./clkcomplicationtemplatecircularsmallstackimage.md)
  A template for displaying an image with a line of text below it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringimage)*