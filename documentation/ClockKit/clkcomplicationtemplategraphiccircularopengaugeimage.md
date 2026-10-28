# CLKComplicationTemplateGraphicCircularOpenGaugeImage

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a full-color circular image, an open gauge, and text.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularOpenGaugeImage
```

```objc
@interface CLKComplicationTemplateGraphicCircularOpenGaugeImage : CLKComplicationTemplateGraphicCircular
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family. [Figure 1](./clkcomplicationtemplategraphiccircularopengaugeimage.md#3030686) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text with an open gauge and an image.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030686@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 22 pixels | 22 pixels |
| 41 mm | 23 pixels | 23 pixels |
| 44 mm | 24 pixels | 24 pixels |
| 45 mm | 26 pixels | 26 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomImageProvider: CLKFullColorImageProvider, centerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccircularopengaugeimage/init%28gaugeprovider,bottomimageprovider,centertextprovider%29.md)
  Creates a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.
- [+ templateWithGaugeProvider:bottomImageProvider:centerTextProvider:](./clkcomplicationtemplategraphiccircularopengaugeimage/templatewithgaugeprovider_bottomimageprovider_centertextprovider_.md)
  Returns a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.
### Setting the Complication Data
- [var bottomImageProvider: CLKFullColorImageProvider](./clkcomplicationtemplategraphiccircularopengaugeimage/bottomimageprovider.md)
  The image to display at the bottom of the gauge.
- [var centerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccircularopengaugeimage/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccircularopengaugeimage/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](./clkcomplicationtemplategraphiccircular.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Open and closed gauges
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](./clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText](./clkcomplicationtemplategraphiccircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with a single piece of text for the gauge.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](./clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeImage](./clkcomplicationtemplategraphiccircularclosedgaugeimage.md)
  A template for displaying a full-color circular image and a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](./clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeText](./clkcomplicationtemplategraphiccircularclosedgaugetext.md)
  A template for displaying text inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeimage)*