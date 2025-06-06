# CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView

**Framework**: ClockKit  
**Kind**: class

A template for displaying an extra-large SwiftUI view inside a closed circular gauge.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularclosedgaugeview#3667262.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the gauge and label.](https://docs-assets.developer.apple.com/published/baef3ceebed0c74015e109cf86775fbf/media-3667262%402x.png)

The table below lists the dimensions of the view displayed by the template. The image provider automatically masks the image to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 77 points | 77 points |
| 41 mm | 81.5 points | 81.5 points |
| 44 mm | 87 points | 87 points |
| 41 mm | 81.5 points | 81.5 points |

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, label: Label)](clkcomplicationtemplategraphicextralargecircularclosedgaugeview/init(gaugeprovider:label:).md)
  Creates a new template with a closed circular gauge and a SwiftUI view in the center.
### Accessing the Content
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicextralargecircularclosedgaugeview/gaugeprovider.md)
  The gauge provider for the template.
- [var label: Label](clkcomplicationtemplategraphicextralargecircularclosedgaugeview/label.md)
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
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugeview)*