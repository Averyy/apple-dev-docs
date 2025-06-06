# CLKComplicationTemplateGraphicCircularClosedGaugeText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text inside a closed circular gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularClosedGaugeText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularclosedgaugetext#3030685.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text surrounded by a closed gauge.](https://docs-assets.developer.apple.com/published/32f3e31d4f77dfb842d910bc37712830/media-3030685%402x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularclosedgaugetext/init(gaugeprovider:centertextprovider:).md)
  Creates a new template that has a closed circular gauge with a small amount of text in the center.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularclosedgaugetext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccircularclosedgaugetext/gaugeprovider.md)
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
- [class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText](clkcomplicationtemplategraphiccircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with a single piece of text for the gauge.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeImage](clkcomplicationtemplategraphiccircularclosedgaugeimage.md)
  A template for displaying a full-color circular image and a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularclosedgaugetext)*