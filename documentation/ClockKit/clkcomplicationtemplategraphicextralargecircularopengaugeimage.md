# CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an extra-large, full-color circular image, an open gauge, and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularopengaugeimage#3667237.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge, text, and image providers.](/images/com.apple.clockkit/media-3667237@2x.png)

The table below lists the dimensions of the image you use in this template. Use @2x images for display on Apple Watch so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 62 pixels | 62 pixels |
| 41 mm | 66 pixels | 66 pixels |
| 44 mm | 66 pixels | 66 pixels |
| 45 mm | 74 pixels | 74 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomImageProvider: CLKFullColorImageProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularopengaugeimage/init(gaugeprovider:bottomimageprovider:centertextprovider:).md)
  Creates a new template with an open circular gauge, an image at the bottom, and text in the center.
### Setting the Complication Data
- [var bottomImageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphicextralargecircularopengaugeimage/bottomimageprovider.md)
  The image to display at the bottom of the gauge.
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugeimage/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularopengaugeimage/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeSimpleText](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with additional text at the bottom of the gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeRangeText](clkcomplicationtemplategraphicextralargecircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with additional leading and trailing text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeImage](clkcomplicationtemplategraphicextralargecircularclosedgaugeimage.md)
  A template for displaying an extra-large, full-color circular image inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText](clkcomplicationtemplategraphicextralargecircularclosedgaugetext.md)
  A template for displaying text inside an extra-large closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugeimage)*