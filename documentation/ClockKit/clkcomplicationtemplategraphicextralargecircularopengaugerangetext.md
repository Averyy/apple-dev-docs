# CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeRangeText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text inside an open gauge, with additional leading and trailing text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeRangeText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularopengaugerangetext#3667406.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge, leading text, trailing text, and center text providers.](https://docs-assets.developer.apple.com/published/c00514f53fc3fe740b51b0b49f5ca2d1/media-3667406%402x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider, trailingTextProvider: CLKTextProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularopengaugerangetext/init(gaugeprovider:leadingtextprovider:trailingtextprovider:centertextprovider:).md)
  Creates a new template that has an open, circular gauge with leading and trailing text, and a central text element.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugerangetext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularopengaugerangetext/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugerangetext/leadingtextprovider.md)
  The text to display on the leading edge of the gauge.
- [var trailingTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugerangetext/trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.

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
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeImage](clkcomplicationtemplategraphicextralargecircularclosedgaugeimage.md)
  A template for displaying an extra-large, full-color circular image inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText](clkcomplicationtemplategraphicextralargecircularclosedgaugetext.md)
  A template for displaying text inside an extra-large closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugerangetext)*