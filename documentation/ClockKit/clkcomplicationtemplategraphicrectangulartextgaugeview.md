# CLKComplicationTemplateGraphicRectangularTextGaugeView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularTextGaugeView<Label> where Label : View
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](./clkcomplicationfamily/graphicrectangular.md) family. [Figure 1](./clkcomplicationtemplategraphicrectangulartextgaugeview.md#3667408) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the header label, text providers, and gauge provider.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667408@2x.png)

The following table lists the dimensions of the SwiftUI view displayed by this template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 12 points | 12 points |
| 41 mm | 12.5 points | 12.5 points |
| 44 mm | 13.5 points | 13.5 points |
| 45 mm | 14.5 points | 14.5 points |

## Topics

### Creating the Template
- [init(headerLabel: Label, headerTextProvider: CLKTextProvider, bodyTextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)](./clkcomplicationtemplategraphicrectangulartextgaugeview/init%28headerlabel,headertextprovider,bodytextprovider,gaugeprovider%29.md)
  Creates a new template that has a header row with a SwiftUI view and text, body text, and a gauge.
### Accessing the Content
- [var headerLabel: Label](./clkcomplicationtemplategraphicrectangulartextgaugeview/headerlabel.md)
  The SwiftUI view displayed by the template.
- [var headerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphicrectangulartextgaugeview/headertextprovider.md)
  The header text to display in the complication.
- [var bodyTextProvider: CLKTextProvider](./clkcomplicationtemplategraphicrectangulartextgaugeview/bodytextprovider.md)
  The main body text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphicrectangulartextgaugeview/gaugeprovider.md)
  The gauge to display in the complication.

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
- [class CLKComplicationTemplateGraphicRectangularLargeView](./clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](./clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgaugeview)*