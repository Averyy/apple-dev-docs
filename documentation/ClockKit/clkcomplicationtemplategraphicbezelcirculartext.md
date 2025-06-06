# CLKComplicationTemplateGraphicBezelCircularText

**Framework**: ClockKit  
**Kind**: class

A template for displaying a circular complication with text along the bezel.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicBezelCircularText
```

#### Overview

The graphic bezel templates display a circular template, and text that wraps around the watch face.

This template belongs to the [`CLKComplicationFamily.graphicBezel`](clkcomplicationfamily/graphicbezel.md) family. [`Figure 1`](clkcomplicationtemplategraphicbezelcirculartext#3030704.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text along the bezel and the circular template.](https://docs-assets.developer.apple.com/published/b3e1d3b34f7459b04787c4cdd7f15288/media-3030704%402x.png)

The text is optional; this template can either display a circular template with text, or the circular template by itself.

## Topics

### Creating the Template
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular)](clkcomplicationtemplategraphicbezelcirculartext/init(circulartemplate:).md)
  Creates a circular template.
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular, textProvider: CLKTextProvider?)](clkcomplicationtemplategraphicbezelcirculartext/init(circulartemplate:textprovider:).md)
  Creates a circular template with text that wraps around the bezel.
### Setting the Complication Data
- [var circularTemplate: CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphicbezelcirculartext/circulartemplate.md)
  The circular template to display.
- [var textProvider: CLKTextProvider?](clkcomplicationtemplategraphicbezelcirculartext/textprovider.md)
  The text to display along the bezel.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Circular complication templates](circular-complication-templates.md)
  Display graphical data in a compact circle.
- [Corner complication templates](corner-complication-templates.md)
  Display graphically rich data in the watch face’s corner.
- [Rectangular complication templates.](rectangular-complication-templates.md)
  Displays large, rectangular complications for charts, images, or multiple lines of text.
- [Extra large circular templates](extra-large-circular-templates.md)
  Display large, easy-to-read content on the X-Large watch face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicbezelcirculartext)*