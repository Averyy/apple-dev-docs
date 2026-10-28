# CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying an extra-large SwiftUI view inside a closed circular gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView<Label> where Label : View
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](./clkcomplicationfamily/graphicextralarge.md) family. [Figure 1](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md#3667262) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge and label.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667262@2x.png)

The table below lists the dimensions of the view displayed by the template. The image provider automatically masks the image to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 77 points | 77 points |
| 41 mm | 81.5 points | 81.5 points |
| 44 mm | 87 points | 87 points |
| 41 mm | 81.5 points | 81.5 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, label: Label)](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview/init%28gaugeprovider,label%29.md)
  Creates a new template with a closed circular gauge and a SwiftUI view in the center.
### Accessing the Content
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var label: Label](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview/label.md)
  The SwiftUI view displayed by the template.

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

### Extra large templates
- [class CLKComplicationTemplateGraphicExtraLargeCircularView](./clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](./clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](./clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugeview)*