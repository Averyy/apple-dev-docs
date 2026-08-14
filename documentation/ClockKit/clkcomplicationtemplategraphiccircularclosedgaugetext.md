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

![Diagram showing the layout of text surrounded by a closed gauge.](/images/com.apple.clockkit/media-3030685@2x.png)

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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

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