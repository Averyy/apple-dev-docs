# CLKComplicationTemplateGraphicCircularView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a circular view.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularView<Content> where Content : View
```

## Mentions

- [Building complications with SwiftUI](building-complications-with-swiftui.md)

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularview#3667259.md) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content.](https://docs-assets.developer.apple.com/published/32ce6ff9d38fbc2d4021860d48742237/media-3667259%402x.png)

The following table lists the dimensions of the view displayed by this template. ClockKit masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 42 points | 42 points |
| 41 mm | 44.5 points | 44.5 points |
| 44 mm | 47 points | 47 points |
| 45 mm | 50 points | 50 points |

## Topics

### Creating the Template
- [init(Content)](clkcomplicationtemplategraphiccircularview/init(_:).md)
  Creates a template that has a circular SwiftUI view.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphiccircularview/content.md)
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

- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularview)*