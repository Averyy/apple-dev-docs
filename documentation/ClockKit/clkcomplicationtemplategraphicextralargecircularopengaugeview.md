# CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view, an open gauge, and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularopengaugeview#3667407.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge provider, text provider, and label.](https://docs-assets.developer.apple.com/published/dc27755e3605a7d64dbdc56e62accdf1/media-3667407%402x.png)

The table below lists the dimensions of the view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 31 points | 31 points |
| 41 mm | 33 points | 33 points |
| 44 mm | 33 points | 33 points |
| 45 mm | 37 points | 37 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider, bottomLabel: Label)](clkcomplicationtemplategraphicextralargecircularopengaugeview/init(gaugeprovider:centertextprovider:bottomlabel:).md)
  Creates a new template that has an open circular gauge, a small amount of text in the center, and a small SwiftUI view at the bottom.
### Accessing the Content
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularopengaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var centerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularopengaugeview/centertextprovider.md)
  The text provider for the center text.
- [var bottomLabel: Label](clkcomplicationtemplategraphicextralargecircularopengaugeview/bottomlabel.md)
  The SwiftUI view displayed by the template.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicExtraLargeCircularView](clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugeview)*