# CLKComplicationTemplateGraphicCornerCircularView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view in the clock face’s corner.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicCornerCircularView<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](./clkcomplicationfamily/graphiccorner.md) family. [Figure 1](./clkcomplicationtemplategraphiccornercircularview.md#3667248) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667248@2x.png)

The following table lists the dimensions of the SwiftUI view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 32 points | 32 points |
| 41 mm | 34 points | 34 points |
| 44 mm | 36 points | 36 points |
| 45 mm | 38 points | 38 points |

## Topics

### Creating the Template
- [init(Content)](./clkcomplicationtemplategraphiccornercircularview/init%28_%29.md)
  Creates a template that has a circular SwiftUI view.
### Accessing the Content
- [var content: Content](./clkcomplicationtemplategraphiccornercircularview/content.md)
  The SwiftUI view displayed by the template.

## Relationships

### Inherits From
- [CLKComplicationTemplate](./clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Corner templates
- [class CLKComplicationTemplateGraphicCornerGaugeView](./clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](./clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornercircularview)*