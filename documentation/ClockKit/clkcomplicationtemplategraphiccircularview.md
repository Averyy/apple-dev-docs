# CLKComplicationTemplateGraphicCircularView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a circular view.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularView<Content> where Content : View
```

## Mentions

- [Building complications with SwiftUI](./building-complications-with-swiftui.md)

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family. [Figure 1](./clkcomplicationtemplategraphiccircularview.md#3667259) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667259@2x.png)

The following table lists the dimensions of the view displayed by this template. ClockKit masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 42 points | 42 points |
| 41 mm | 44.5 points | 44.5 points |
| 44 mm | 47 points | 47 points |
| 45 mm | 50 points | 50 points |

## Topics

### Creating the Template
- [init(Content)](./clkcomplicationtemplategraphiccircularview/init%28_%29.md)
  Creates a template that has a circular SwiftUI view.
### Accessing the Content
- [var content: Content](./clkcomplicationtemplategraphiccircularview/content.md)
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
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](./clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](./clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularStackViewText](./clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularview)*