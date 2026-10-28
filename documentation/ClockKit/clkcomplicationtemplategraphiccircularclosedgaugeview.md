# CLKComplicationTemplateGraphicCircularClosedGaugeView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view inside a closed circular gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularClosedGaugeView<Label> where Label : View
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family. [Figure 1](./clkcomplicationtemplategraphiccircularclosedgaugeview.md#3667247) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge provider and the label.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667247@2x.png)

The following table lists the dimensions of the SwiftUI view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 27 points | 27 points |
| 41 mm | 28.5 points | 28.5 points |
| 44 mm | 31 points | 31 points |
| 45 mm | 32 points | 32 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, label: Label)](./clkcomplicationtemplategraphiccircularclosedgaugeview/init%28gaugeprovider,label%29.md)
  Creates a new template with a closed circular gauge, and a SwiftUI view in the center.
### Accessing the Content
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccircularclosedgaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var label: Label](./clkcomplicationtemplategraphiccircularclosedgaugeview/label.md)
  The SwiftUI view displayed by the template.

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

### Circular templates
- [class CLKComplicationTemplateGraphicCircularView](./clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](./clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularStackViewText](./clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularclosedgaugeview)*