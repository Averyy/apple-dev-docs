# CLKComplicationTemplateGraphicCircularClosedGaugeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view inside a closed circular gauge.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularClosedGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularclosedgaugeview#3667247.md) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge provider and the label.](https://docs-assets.developer.apple.com/published/a992c4ec1dbea3fd8c185c6639dbb350/media-3667247%402x.png)

The following table lists the dimensions of the SwiftUI view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 27 points | 27 points |
| 41 mm | 28.5 points | 28.5 points |
| 44 mm | 31 points | 31 points |
| 45 mm | 32 points | 32 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, label: Label)](clkcomplicationtemplategraphiccircularclosedgaugeview/init(gaugeprovider:label:).md)
  Creates a new template with a closed circular gauge, and a SwiftUI view in the center.
### Accessing the Content
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccircularclosedgaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var label: Label](clkcomplicationtemplategraphiccircularclosedgaugeview/label.md)
  The SwiftUI view displayed by the template.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphiccircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularclosedgaugeview)*