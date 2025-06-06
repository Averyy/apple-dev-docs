# CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text inside an extra-large closed circular gauge.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularclosedgaugetext#3667235.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge and text providers.](https://docs-assets.developer.apple.com/published/54e6868ad36ec430524a6df96896c85d/media-3667235%402x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularclosedgaugetext/init(gaugeprovider:centertextprovider:).md)
  Creates a new template with a closed circular gauge with text in the center.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularclosedgaugetext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularclosedgaugetext/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeImage](clkcomplicationtemplategraphicextralargecircularopengaugeimage.md)
  A template for displaying an extra-large, full-color circular image, an open gauge, and text.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugetext)*