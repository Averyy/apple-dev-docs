# CLKComplicationTemplateGraphicCornerTextView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view and text in the clock face’s corner.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicCornerTextView<Label> where Label : View
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](./clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the text provider and label.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667263@2x.png)

The following table lists the dimensions of the view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 20 points | 20 points |
| 41 mm | 21 points | 21 points |
| 44 mm | 22 points | 22 points |
| 45 mm | 24 points | 24 points |

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, label: Label)](./clkcomplicationtemplategraphiccornertextview/init%28textprovider,label%29.md)
  Creates a template with a line of text and a SwiftUI view.
### Accessing the Content
- [var textProvider: CLKTextProvider](./clkcomplicationtemplategraphiccornertextview/textprovider.md)
  The text provider for the text.
- [var label: Label](./clkcomplicationtemplategraphiccornertextview/label.md)
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
- [class CLKComplicationTemplateGraphicCornerCircularView](./clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeView](./clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextview)*