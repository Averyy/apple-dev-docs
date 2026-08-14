# CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeSimpleText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text inside an open gauge, with additional text at the bottom of the gauge.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeSimpleText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext#3667232.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge, center text, and bottom text providers.](/images/com.apple.clockkit/media-3667232@2x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomTextProvider: CLKTextProvider, centerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext/init(gaugeprovider:bottomtextprovider:centertextprovider:).md)
  Creates a new template with an open circular gauge, a small text element at the bottom, and a larger text element in the center.
### Setting the Complication Data
- [var bottomTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext/bottomtextprovider.md)
  The text to display at the bottom of the gauge.
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularopengaugesimpletext/gaugeprovider.md)
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

- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeImage](clkcomplicationtemplategraphicextralargecircularopengaugeimage.md)
  A template for displaying an extra-large, full-color circular image, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeRangeText](clkcomplicationtemplategraphicextralargecircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with additional leading and trailing text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeImage](clkcomplicationtemplategraphicextralargecircularclosedgaugeimage.md)
  A template for displaying an extra-large, full-color circular image inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText](clkcomplicationtemplategraphicextralargecircularclosedgaugetext.md)
  A template for displaying text inside an extra-large closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugesimpletext)*