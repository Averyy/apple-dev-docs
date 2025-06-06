# CLKComplicationTemplateGraphicCircularOpenGaugeImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a full-color circular image, an open gauge, and text.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularOpenGaugeImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularopengaugeimage#3030686.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text with an open gauge and an image.](https://docs-assets.developer.apple.com/published/f3311597476f991aee2e6aa226e19dd4/media-3030686%402x.png)

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
- [init(gaugeProvider: CLKGaugeProvider, bottomImageProvider: CLKFullColorImageProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularopengaugeimage/init(gaugeprovider:bottomimageprovider:centertextprovider:).md)
  Creates a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.
### Setting the Complication Data
- [var bottomImageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccircularopengaugeimage/bottomimageprovider.md)
  The image to display at the bottom of the gauge.
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularopengaugeimage/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccircularopengaugeimage/gaugeprovider.md)
  The gauge to display in the complication.

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

- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText](clkcomplicationtemplategraphiccircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with a single piece of text for the gauge.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeImage](clkcomplicationtemplategraphiccircularclosedgaugeimage.md)
  A template for displaying a full-color circular image and a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeText](clkcomplicationtemplategraphiccircularclosedgaugetext.md)
  A template for displaying text inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeimage)*