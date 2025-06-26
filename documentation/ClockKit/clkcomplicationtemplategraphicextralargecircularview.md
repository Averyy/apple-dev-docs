# CLKComplicationTemplateGraphicExtraLargeCircularView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a circular SwiftUI view.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularView<Content> where Content : View
```

## Mentions

- [Building complications with SwiftUI](building-complications-with-swiftui.md)
- [Adding text to a complication](adding-text-to-a-complication.md)

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularview#3667292.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content.](https://docs-assets.developer.apple.com/published/a9bf2d2b73337043e1cc6c75892c2b4f/media-3667292%402x.png)

The table below lists the dimensions of the view displayed by the template. The template automatically masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 120 points | 120 points |
| 41 mm | 127 points | 127 points |
| 44 mm | 132 points | 132 points |
| 45 mm | 143 points | 143 points |

## Topics

### Creating the Template
- [init(Content)](clkcomplicationtemplategraphicextralargecircularview/init(_:).md)
  Creates a template that has a circular view.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphicextralargecircularview/content.md)
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

- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularview)*