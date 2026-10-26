# CLKComplicationTemplateGraphicCornerGaugeImage

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying an image and a gauge in the clock face’s corner.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerGaugeImage
```

```objc
@interface CLKComplicationTemplateGraphicCornerGaugeImage : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](./clkcomplicationfamily/graphiccorner.md) family. [Figure 1](./clkcomplicationtemplategraphiccornergaugeimage.md#3030693) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of an image and a gauge with trailing text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030693@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 40 pixels | 40 pixels |
| 41 mm | 42 pixels | 42 pixels |
| 44 mm | 44 pixels | 44 pixels |
| 45 mm | 48 pixels | 48 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](./clkcomplicationtemplategraphiccornergaugeimage/init%28gaugeprovider,imageprovider%29.md)
  Creates a new template that has a gauge and an image.
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, imageProvider: CLKFullColorImageProvider)](./clkcomplicationtemplategraphiccornergaugeimage/init%28gaugeprovider,leadingtextprovider,trailingtextprovider,imageprovider%29.md)
  Creates a new template that has a gauge with leading and trailing text and an image.
- [+ templateWithGaugeProvider:imageProvider:](./clkcomplicationtemplategraphiccornergaugeimage/templatewithgaugeprovider_imageprovider_.md)
  Returns a new template that has a gauge and an image.
- [+ templateWithGaugeProvider:leadingTextProvider:trailingTextProvider:imageProvider:](./clkcomplicationtemplategraphiccornergaugeimage/templatewithgaugeprovider_leadingtextprovider_trailingtextprovider_imageprovider_.md)
  Returns a new template that has a gauge with leading and trailing text and an image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](./clkcomplicationtemplategraphiccornergaugeimage/imageprovider.md)
  The image to display.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccornergaugeimage/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./clkcomplicationtemplategraphiccornergaugeimage/leadingtextprovider.md)
  The text to display on the leading edge of the gauge.
- [var trailingTextProvider: CLKTextProvider?](./clkcomplicationtemplategraphiccornergaugeimage/trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.

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

### Gauges
- [class CLKComplicationTemplateGraphicCornerGaugeView](./clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeText](./clkcomplicationtemplategraphiccornergaugetext.md)
  A template for displaying text and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage)*