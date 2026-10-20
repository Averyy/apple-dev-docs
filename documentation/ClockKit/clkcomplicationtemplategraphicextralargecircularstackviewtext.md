# CLKComplicationTemplateGraphicExtraLargeCircularStackViewText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view and text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](./clkcomplicationfamily/graphicextralarge.md) family. [Figure 1](./clkcomplicationtemplategraphicextralargecircularstackviewtext.md#3667264) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content and text provider.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667264@2x.png)

The table below lists the dimensions of the view displayed by the template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 40 points | 20 points |
| 44 mm | 43.5 points | 22 points |

## Topics

### Creating the Template
- [init(content: Content, textProvider: CLKTextProvider)](./clkcomplicationtemplategraphicextralargecircularstackviewtext/init%28content,textprovider%29.md)
  Creates a template that has a view and a small amount of text.
### Accessing the Content
- [var content: Content](./clkcomplicationtemplategraphicextralargecircularstackviewtext/content.md)
  The SwiftUI view displayed by the template.
- [var textProvider: CLKTextProvider](./clkcomplicationtemplategraphicextralargecircularstackviewtext/textprovider.md)
  The text to display below the view.

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
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](./clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstackviewtext)*