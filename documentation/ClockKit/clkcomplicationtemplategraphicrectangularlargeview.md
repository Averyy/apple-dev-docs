# CLKComplicationTemplateGraphicRectangularLargeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a large rectangle containing header text and a SwiftUI view.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularLargeView<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangularlargeview#3667291.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the header text provider and the content.](https://docs-assets.developer.apple.com/published/fbf3033f3c174c4ab879d308bbc54929/media-3667291%402x.png)

The following table lists the dimensions of the view displayed by this template. The template automatically masks the view to a rounded rectangle with a 8-pixel corner radius.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 150 points | 47 points |
| 41 mm | 159 points | 50 points |
| 44 mm | 171 points | 54 points |
| 45 mm | 178.5 points | 56 points |

## Topics

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, content: Content)](clkcomplicationtemplategraphicrectangularlargeview/init(headertextprovider:content:).md)
  Creates a new template with a text provider and a SwiftUI view.
### Accessing the Content
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularlargeview/headertextprovider.md)
  The text provider for a row of text.
- [var content: Content](clkcomplicationtemplategraphicrectangularlargeview/content.md)
  The SwiftUI view displayed by the template.

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
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularlargeview)*