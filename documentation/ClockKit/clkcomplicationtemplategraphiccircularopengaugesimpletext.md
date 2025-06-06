# CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text inside an open gauge, with a single piece of text for the gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularopengaugesimpletext#3030688.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text with an open gauge and subtext.](https://docs-assets.developer.apple.com/published/0e9d17c5ed021bd768132dfdfedbfdc4/media-3030688%402x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomTextProvider: CLKTextProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularopengaugesimpletext/init(gaugeprovider:bottomtextprovider:centertextprovider:).md)
  Creates a new template with an open circular gauge, a small text element at the bottom, and a larger text element in the center.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularopengaugesimpletext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var bottomTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularopengaugesimpletext/bottomtextprovider.md)
  The text to display at the bottom of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccircularopengaugesimpletext/gaugeprovider.md)
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

- [class CLKComplicationTemplateGraphicCircularOpenGaugeImage](clkcomplicationtemplategraphiccircularopengaugeimage.md)
  A template for displaying a full-color circular image, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeImage](clkcomplicationtemplategraphiccircularclosedgaugeimage.md)
  A template for displaying a full-color circular image and a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeText](clkcomplicationtemplategraphiccircularclosedgaugetext.md)
  A template for displaying text inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugesimpletext)*