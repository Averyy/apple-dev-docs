# CLKComplicationTemplateGraphicRectangularStandardBodyView

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a SwiftUI label and up to three rows of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularStandardBodyView<Label> where Label : View
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](./clkcomplicationfamily/graphicrectangular.md) family.  shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the header label and text providers.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667290@2x.png)

The following table lists the dimensions of the image you use in this template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 12 points | 12 points |
| 41 mm | 12.5 points | 12.5 points |
| 44 mm | 13.5 points | 13.5 points |
| 45 mm | 14.5 points | 14.5 points |

## Topics

### Creating the Template
- [init(headerLabel: Label, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./clkcomplicationtemplategraphicrectangularstandardbodyview/init%28headerlabel,headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a header row with a SwiftUI view and text, and two rows of body text.
### Accessing the Content
- [var headerLabel: Label](./clkcomplicationtemplategraphicrectangularstandardbodyview/headerlabel.md)
  The SwiftUI view displayed by the template.
- [var headerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphicrectangularstandardbodyview/headertextprovider.md)
  The text provider for the header text.
- [var body1TextProvider: CLKTextProvider](./clkcomplicationtemplategraphicrectangularstandardbodyview/body1textprovider.md)
  The text provider for the first row of body text.
- [var body2TextProvider: CLKTextProvider?](./clkcomplicationtemplategraphicrectangularstandardbodyview/body2textprovider.md)
  The text provider for the second row of body text.

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
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](./clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.
- [class CLKComplicationTemplateGraphicRectangularLargeView](./clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](./clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbodyview)*