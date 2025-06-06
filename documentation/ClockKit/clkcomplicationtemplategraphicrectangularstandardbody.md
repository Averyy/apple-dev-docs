# CLKComplicationTemplateGraphicRectangularStandardBody

**Framework**: ClockKit  
**Kind**: class

A template for displaying a large rectangle containing text.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicRectangularStandardBody
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangularstandardbody#3030705.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of header text and two rows of body text.](https://docs-assets.developer.apple.com/published/2d7fb5d4bf5befa1e4dee9ff87c430ab/media-3030705%402x.png)

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
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplategraphicrectangularstandardbody/init(headertextprovider:body1textprovider:).md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplategraphicrectangularstandardbody/init(headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplategraphicrectangularstandardbody/init(headerimageprovider:headertextprovider:body1textprovider:).md)
  Creates a new template that has a header row with an image and text, and a row of body text.
- [init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplategraphicrectangularstandardbody/init(headerimageprovider:headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a header row with an image and text, and two rows of body text.
### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbody/headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](clkcomplicationtemplategraphicrectangularstandardbody/headerimageprovider.md)
  The header image to display.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbody/body1textprovider.md)
  The main body text to display in the complication.
- [var body2TextProvider: CLKTextProvider?](clkcomplicationtemplategraphicrectangularstandardbody/body2textprovider.md)
  The secondary body text to display in the complication.

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

- [class CLKComplicationTemplateGraphicRectangularStandardBodyView](clkcomplicationtemplategraphicrectangularstandardbodyview.md)
  A template for displaying a SwiftUI label and up to three rows of text.
- [class CLKComplicationTemplateGraphicRectangularTextGauge](clkcomplicationtemplategraphicrectangulartextgauge.md)
  A template for displaying a large rectangle containing text and a gauge.
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbody)*