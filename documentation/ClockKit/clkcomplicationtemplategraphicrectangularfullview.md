# CLKComplicationTemplateGraphicRectangularFullView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI view that fills the entire template.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularFullView<Content> where Content : View
```

## Mentions

- [Building complications with SwiftUI](./building-complications-with-swiftui.md)

## Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](./clkcomplicationfamily/graphicrectangular.md) family. [Figure 1](./clkcomplicationtemplategraphicrectangularfullview.md#3667288) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content and the safe area insets.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667288@2x.png)

The following table lists the dimensions of the view displayed by this template. The template automatically masks the view to a rounded rectangle with a 8-pixel corner radius. By default, the template also provides a safe area inset to help you avoid clipping your content. Use the [`edgesIgnoringSafeArea(_:)`](../SwiftUI/view/edgesignoringsafearea%28_%29.md) modifier if you need to fill the complication to the edges.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm (safe area inset) | 150 points | 57 points |
| 40 mm (full view) | 162 points | 69 points |
| 41 mm (safe area inset) | 158.5 points | 60 points |
| 41 mm (full view) | 171.5 points | 73 points |
| 44 mm (safe area inset) | 171 points | 65 points |
| 44 mm (full view) | 184 points | 78 points |
| 45 mm (safe area inset) | 179 points | 68 points |
| 45 mm (full view) | 193 points | 82 points |

## Topics

### Creating the Template
- [init(Content)](./clkcomplicationtemplategraphicrectangularfullview/init%28_%29.md)
  Creates a template that has a circular image.
### Accessing the Content
- [var content: Content](./clkcomplicationtemplategraphicrectangularfullview/content.md)
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

### Rectangular templates
- [class CLKComplicationTemplateGraphicRectangularStandardBodyView](./clkcomplicationtemplategraphicrectangularstandardbodyview.md)
  A template for displaying a SwiftUI label and up to three rows of text.
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](./clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.
- [class CLKComplicationTemplateGraphicRectangularLargeView](./clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularfullview)*