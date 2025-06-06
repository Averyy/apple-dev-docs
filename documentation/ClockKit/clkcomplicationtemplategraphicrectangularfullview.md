# CLKComplicationTemplateGraphicRectangularFullView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view that fills the entire template.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicRectangularFullView<Content> where Content : View
```

## Mentions

- [Building complications with SwiftUI](building-complications-with-swiftui.md)

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangularfullview#3667288.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content and the safe area insets.](https://docs-assets.developer.apple.com/published/a8a67b1cfbffd5ea77d58b9b25204045/media-3667288%402x.png)

The following table lists the dimensions of the view displayed by this template. The template automatically masks the view to a rounded rectangle with a 8-pixel corner radius. By default, the template also provides a safe area inset to help you avoid clipping your content. Use the [`edgesIgnoringSafeArea(_:)`](https://developer.apple.com/documentation/SwiftUI/View/edgesIgnoringSafeArea(_:)) modifier if you need to fill the complication to the edges.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm (safe area inset) | 150 points | 57 points |
| 40 mm (full view) | 162 points | 69 points |
| 41 mm (safe area inset) | 158.5 points | 60 points |
| 41 mm (full view) | 171.5 points | 73 points |
| 44 mm (safe area inset) | 171 points | 65 points |
| 44 mm (full view) | 184 points | 78 points |
| 45 mm (safe area inset) | 179 points | 68 points |
| 45 mm (full view) | 193 points | 82 points |

## Topics

### Creating the Template
- [init(Content)](clkcomplicationtemplategraphicrectangularfullview/init(_:).md)
  Creates a template that has a circular image.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphicrectangularfullview/content.md)
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
- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularfullview)*