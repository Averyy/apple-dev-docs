# CLKComplicationTemplateGraphicCircularClosedGaugeText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying text inside a closed circular gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularClosedGaugeText
```

```objc
@interface CLKComplicationTemplateGraphicCircularClosedGaugeText : CLKComplicationTemplateGraphicCircular
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family. [Figure 1](./clkcomplicationtemplategraphiccircularclosedgaugetext.md#3030685) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text surrounded by a closed gauge.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030685@2x.png)

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccircularclosedgaugetext/init%28gaugeprovider,centertextprovider%29.md)
  Creates a new template that has a closed circular gauge with a small amount of text in the center.
- [+ templateWithGaugeProvider:centerTextProvider:](./clkcomplicationtemplategraphiccircularclosedgaugetext/templatewithgaugeprovider_centertextprovider_.md)
  Returns a new template that has a closed circular gauge with a small amount of text in the center.
### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccircularclosedgaugetext/centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccircularclosedgaugetext/gaugeprovider.md)
  The gauge to display in the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](./clkcomplicationtemplategraphiccircular.md)
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
- [class CLKComplicationTemplateGraphicCircularOpenGaugeImage](./clkcomplicationtemplategraphiccircularopengaugeimage.md)
  A template for displaying a full-color circular image, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](./clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeSimpleText](./clkcomplicationtemplategraphiccircularopengaugesimpletext.md)
  A template for displaying text inside an open gauge, with a single piece of text for the gauge.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeRangeText](./clkcomplicationtemplategraphiccircularopengaugerangetext.md)
  A template for displaying text inside an open gauge, with leading and trailing text for the gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeImage](./clkcomplicationtemplategraphiccircularclosedgaugeimage.md)
  A template for displaying a full-color circular image and a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](./clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularclosedgaugetext)*