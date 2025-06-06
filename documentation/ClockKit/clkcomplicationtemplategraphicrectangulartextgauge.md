# CLKComplicationTemplateGraphicRectangularTextGauge

**Framework**: ClockKit  
**Kind**: class

A template for displaying a large rectangle containing text and a gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicRectangularTextGauge
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangulartextgauge#3030706.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of a header image, header text, body text, and a gauge.](https://docs-assets.developer.apple.com/published/4095e05f1e6e9e5453a8180a33325f81/media-3030706%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 24 pixels | 24 pixels |
| 41 mm | 25 pixels | 25 pixels |
| 44 mm | 27 pixels | 27 pixels |
| 45 mm | 29 pixels | 29 pixels |

This template supports full-color images.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)](clkcomplicationtemplategraphicrectangulartextgauge/init(headertextprovider:body1textprovider:gaugeprovider:).md)
  Creates a new template that has header text, body text, and a gauge.
- [init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)](clkcomplicationtemplategraphicrectangulartextgauge/init(headerimageprovider:headertextprovider:body1textprovider:gaugeprovider:).md)
  Creates a new template that has a header row with an image and text, body text, and a gauge.
### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangulartextgauge/headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](clkcomplicationtemplategraphicrectangulartextgauge/headerimageprovider.md)
  The header image to display.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangulartextgauge/body1textprovider.md)
  The main body text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicrectangulartextgauge/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicRectangularStandardBody](clkcomplicationtemplategraphicrectangularstandardbody.md)
  A template for displaying a large rectangle containing text.
- [class CLKComplicationTemplateGraphicRectangularStandardBodyView](clkcomplicationtemplategraphicrectangularstandardbodyview.md)
  A template for displaying a SwiftUI label and up to three rows of text.
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge)*