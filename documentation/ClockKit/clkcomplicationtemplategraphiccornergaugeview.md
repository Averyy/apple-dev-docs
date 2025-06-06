# CLKComplicationTemplateGraphicCornerGaugeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view and a gauge in the clock face’s corner.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCornerGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family. [`Figure 1`](clkcomplicationtemplategraphiccornergaugeview#3667261.md) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge provider, text provider, and label.](https://docs-assets.developer.apple.com/published/d9fc1ea682444269e217e05bd16f84c7/media-3667261%402x.png)

The following table lists the dimensions of the view displayed by this template. ClockKIt masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 20 points | 20 points |
| 41 mm | 21 points | 21 points |
| 44 mm | 22 points | 22 points |
| 45 mm | 24 points | 24 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, label: Label)](clkcomplicationtemplategraphiccornergaugeview/init(gaugeprovider:leadingtextprovider:trailingtextprovider:label:).md)
  Creates a new template with the provided gauge and view.
### Accessing the Content
- [var label: Label](clkcomplicationtemplategraphiccornergaugeview/label.md)
  The SwiftUI view displayed by the template.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccornergaugeview/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugeview/leadingtextprovider.md)
  The text provider for the gauge’s leading text.
- [var trailingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugeview/trailingtextprovider.md)
  The text provider for the gauge’s trailing text.

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

- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeview)*