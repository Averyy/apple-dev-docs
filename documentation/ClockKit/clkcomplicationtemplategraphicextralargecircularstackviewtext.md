# CLKComplicationTemplateGraphicExtraLargeCircularStackViewText

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularstackviewtext#3667264.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content and text provider.](https://docs-assets.developer.apple.com/published/5b1efb6bd81e76e04fa5a2428f4b9c58/media-3667264%402x.png)

The table below lists the dimensions of the view displayed by the template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 40 points | 20 points |
| 44 mm | 43.5 points | 22 points |

## Topics

### Creating the Template
- [init(content: Content, textProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularstackviewtext/init(content:textprovider:).md)
  Creates a template that has a view and a small amount of text.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphicextralargecircularstackviewtext/content.md)
  The SwiftUI view displayed by the template.
- [var textProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularstackviewtext/textprovider.md)
  The text to display below the view.

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
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstackviewtext)*