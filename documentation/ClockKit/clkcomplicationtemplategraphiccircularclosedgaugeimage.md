# CLKComplicationTemplateGraphicCircularClosedGaugeImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a full-color circular image and a closed circular gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularClosedGaugeImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularclosedgaugeimage#3034028.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of a circular image with a closed gauge.](https://docs-assets.developer.apple.com/published/a53f82c65ffb3871744ab47980e84afd/media-3034028%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 54 pixels | 54 pixels |
| 41 mm | 57 pixels | 57 pixels |
| 44 mm | 62 pixels | 62 pixels |
| 45 mm | 64 pixels | 64 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Tempate
- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccircularclosedgaugeimage/init(gaugeprovider:imageprovider:).md)
  Creates a new template with a closed circular gauge, and an image in the center.
### Setting the Complication Data
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccircularclosedgaugeimage/gaugeprovider.md)
  The gauge to display in the complication.
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccircularclosedgaugeimage/imageprovider.md)
  The image to display.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphiccircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCircularOpenGaugeImage](clkcomplicationtemplategraphiccircularopengaugeimage.md)
  A template for displaying a full-color circular image, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText](clkcomplicationtemplategraphiccircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with a single piece of text for the gauge.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeText](clkcomplicationtemplategraphiccircularclosedgaugetext.md)
  A template for displaying text inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularclosedgaugeimage)*