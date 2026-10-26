# CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying text inside an extra-large closed circular gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText
```

```objc
@interface CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeText : CLKComplicationTemplateGraphicExtraLargeCircular
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](./clkcomplicationfamily/graphicextralarge.md) family. [Figure 1](./clkcomplicationtemplategraphicextralargecircularclosedgaugetext.md#3667235) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge and text providers.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667235@2x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphicextralargecircularclosedgaugetext/init%28gaugeprovider,centertextprovider%29.md)
  Creates a new template with a closed circular gauge with text in the center.
- [+ templateWithGaugeProvider:centerTextProvider:](./clkcomplicationtemplategraphicextralargecircularclosedgaugetext/templatewithgaugeprovider_centertextprovider_.md)
  Returns a new template with a closed circular gauge with text in the center.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphicextralargecircularclosedgaugetext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphicextralargecircularclosedgaugetext/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](./clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Open and closed gauges
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeImage](./clkcomplicationtemplategraphicextralargecircularopengaugeimage.md)
  A template for displaying an extra-large, full-color circular image, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](./clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeSimpleText](./clkcomplicationtemplategraphicextralargecircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with additional text at the bottom of the gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeRangeText](./clkcomplicationtemplategraphicextralargecircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with additional leading and trailing text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeImage](./clkcomplicationtemplategraphicextralargecircularclosedgaugeimage.md)
  A template for displaying an extra-large, full-color circular image inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugetext)*