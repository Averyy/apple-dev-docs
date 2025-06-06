# CLKComplicationTemplateGraphicRectangularTextGaugeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularTextGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangulartextgaugeview#3667408.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the header label, text providers, and gauge provider.](https://docs-assets.developer.apple.com/published/fa5cfc4140640679d83e7d86e7a0c9a0/media-3667408%402x.png)

The following table lists the dimensions of the SwiftUI view displayed by this template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 12 points | 12 points |
| 41 mm | 12.5 points | 12.5 points |
| 44 mm | 13.5 points | 13.5 points |
| 45 mm | 14.5 points | 14.5 points |

## Topics

### Creating the Template
- [init(headerLabel: Label, headerTextProvider: CLKTextProvider, bodyTextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)](clkcomplicationtemplategraphicrectangulartextgaugeview/init(headerlabel:headertextprovider:bodytextprovider:gaugeprovider:).md)
  Creates a new template that has a header row with a SwiftUI view and text, body text, and a gauge.
### Accessing the Content
- [var headerLabel: Label](clkcomplicationtemplategraphicrectangulartextgaugeview/headerlabel.md)
  The SwiftUI view displayed by the template.
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangulartextgaugeview/headertextprovider.md)
  The header text to display in the complication.
- [var bodyTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangulartextgaugeview/bodytextprovider.md)
  The main body text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicrectangulartextgaugeview/gaugeprovider.md)
  The gauge to display in the complication.

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

- [class CLKComplicationTemplateGraphicRectangularStandardBodyView](clkcomplicationtemplategraphicrectangularstandardbodyview.md)
  A template for displaying a SwiftUI label and up to three rows of text.
- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgaugeview)*