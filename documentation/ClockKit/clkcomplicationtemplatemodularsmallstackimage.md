# CLKComplicationTemplateModularSmallStackImage

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a single image with a short line of text below it.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularSmallStackImage
```

```objc
@interface CLKComplicationTemplateModularSmallStackImage : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](./clkcomplicationfamily/modularsmall.md) family.

![Diagram showing the layout of a small image positioned above a short line of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933753@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 52 pixels maximum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 28 pixels |
| 40 mm | 58 pixels maximum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 30 pixels |
| 41 mm | 61 pixels ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 32 pixels |
| 42 mm | 58 pixels maximum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 30 pixels |
| 44 mm | 64 pixels maximum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 34 pixels |
| 45 mm | 69 pixels ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) (You may specify images with a smaller width.) | 36 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(line1ImageProvider: CLKImageProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularsmallstackimage/init%28line1imageprovider,line2textprovider%29.md)
  Creates a new template from the provided image and text.
- [+ templateWithLine1ImageProvider:line2TextProvider:](./clkcomplicationtemplatemodularsmallstackimage/templatewithline1imageprovider_line2textprovider_.md)
  Returns a new template from the provided image and text.
### Setting the Complication Data
- [var line1ImageProvider: CLKImageProvider](./clkcomplicationtemplatemodularsmallstackimage/line1imageprovider.md)
  The image to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallstackimage/line2textprovider.md)
  The text to display on the bottom line of the complication.
- [var highlightLine2: Bool](./clkcomplicationtemplatemodularsmallstackimage/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.

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
- [class CLKComplicationTemplateModularSmallRingImage](./clkcomplicationtemplatemodularsmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallSimpleImage](./clkcomplicationtemplatemodularsmallsimpleimage.md)
  A template for displaying an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstackimage)*