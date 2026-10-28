# CLKComplicationTemplateGraphicExtraLargeCircularView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a circular SwiftUI view.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularView<Content> where Content : View
```

## Mentions

- [Adding text to a complication](./adding-text-to-a-complication.md)
- [Building complications with SwiftUI](./building-complications-with-swiftui.md)

## Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](./clkcomplicationfamily/graphicextralarge.md) family. [Figure 1](./clkcomplicationtemplategraphicextralargecircularview.md#3667292) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667292@2x.png)

The table below lists the dimensions of the view displayed by the template. The template automatically masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 120 points | 120 points |
| 41 mm | 127 points | 127 points |
| 44 mm | 132 points | 132 points |
| 45 mm | 143 points | 143 points |

## Topics

### Creating the Template
- [init(Content)](./clkcomplicationtemplategraphicextralargecircularview/init%28_%29.md)
  Creates a template that has a circular view.
### Accessing the Content
- [var content: Content](./clkcomplicationtemplategraphicextralargecircularview/content.md)
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
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](./clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](./clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularview)*