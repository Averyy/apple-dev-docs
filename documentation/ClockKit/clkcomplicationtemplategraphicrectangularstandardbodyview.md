# CLKComplicationTemplateGraphicRectangularStandardBodyView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI label and up to three rows of text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularStandardBodyView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family.  shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the header label and text providers.](https://docs-assets.developer.apple.com/published/a136876f538eec43e828b1dc80cde268/media-3667290%402x.png)

The following table lists the dimensions of the image you use in this template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 12 points | 12 points |
| 41 mm | 12.5 points | 12.5 points |
| 44 mm | 13.5 points | 13.5 points |
| 45 mm | 14.5 points | 14.5 points |

## Topics

### Creating the Template
- [init(headerLabel: Label, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplategraphicrectangularstandardbodyview/init(headerlabel:headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a header row with a SwiftUI view and text, and two rows of body text.
### Accessing the Content
- [var headerLabel: Label](clkcomplicationtemplategraphicrectangularstandardbodyview/headerlabel.md)
  The SwiftUI view displayed by the template.
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbodyview/headertextprovider.md)
  The text provider for the header text.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbodyview/body1textprovider.md)
  The text provider for the first row of body text.
- [var body2TextProvider: CLKTextProvider?](clkcomplicationtemplategraphicrectangularstandardbodyview/body2textprovider.md)
  The text provider for the second row of body text.

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

- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.
- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbodyview)*