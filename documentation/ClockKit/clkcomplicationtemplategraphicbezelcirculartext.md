# CLKComplicationTemplateGraphicBezelCircularText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a circular complication with text along the bezel.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicBezelCircularText
```

```objc
@interface CLKComplicationTemplateGraphicBezelCircularText : CLKComplicationTemplate
```

#### Overview

The graphic bezel templates display a circular template, and text that wraps around the watch face.

This template belongs to the [`CLKComplicationFamily.graphicBezel`](./clkcomplicationfamily/graphicbezel.md) family. [Figure 1](./clkcomplicationtemplategraphicbezelcirculartext.md#3030704) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text along the bezel and the circular template.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030704@2x.png)

The text is optional; this template can either display a circular template with text, or the circular template by itself.

## Topics

### Creating the Template
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular)](./clkcomplicationtemplategraphicbezelcirculartext/init%28circulartemplate%29.md)
  Creates a circular template.
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular, textProvider: CLKTextProvider?)](./clkcomplicationtemplategraphicbezelcirculartext/init%28circulartemplate,textprovider%29.md)
  Creates a circular template with text that wraps around the bezel.
### Setting the Complication Data
- [var circularTemplate: CLKComplicationTemplateGraphicCircular](./clkcomplicationtemplategraphicbezelcirculartext/circulartemplate.md)
  The circular template to display.
- [var textProvider: CLKTextProvider?](./clkcomplicationtemplategraphicbezelcirculartext/textprovider.md)
  The text to display along the bezel.

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

### Graphic template families
- [Circular complication templates](./circular-complication-templates.md)
  Display graphical data in a compact circle.
- [Corner complication templates](./corner-complication-templates.md)
  Display graphically rich data in the watch face’s corner.
- [Rectangular complication templates.](./rectangular-complication-templates.md)
  Displays large, rectangular complications for charts, images, or multiple lines of text.
- [Extra large circular templates](./extra-large-circular-templates.md)
  Display large, easy-to-read content on the X-Large watch face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicbezelcirculartext)*