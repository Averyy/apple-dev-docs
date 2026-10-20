# CLKComplicationTemplateGraphicCircularOpenGaugeView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view, an open gauge, and text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularOpenGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family. [Figure 1](./clkcomplicationtemplategraphiccircularopengaugeview.md#3667249) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge provider, text provider, and label.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667249@2x.png)

The following table lists the dimensions of the view displayed by this template. The image provider automatically masks the image to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 11 points | 11 points |
| 41 mm | 11.5 points | 11.5 points |
| 44 mm | 12 points | 12 points |
| 45 mm | 13 points | 13 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider, bottomLabel: Label)](./clkcomplicationtemplategraphiccircularopengaugeview/init%28gaugeprovider,centertextprovider,bottomlabel%29.md)
  Creates a new template that has an open circular gauge, a small amount of text in the center, and a small SwiftUI view at the bottom.
### Accesing the Content
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccircularopengaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var centerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccircularopengaugeview/centertextprovider.md)
  The text provider for the center text.
- [var bottomLabel: Label](./clkcomplicationtemplategraphiccircularopengaugeview/bottomlabel.md)
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
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](./clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularStackViewText](./clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeview)*