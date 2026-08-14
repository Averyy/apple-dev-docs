# CLKComplicationTemplateGraphicCircularStackViewText

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCircularStackViewText<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularstackviewtext#3667405.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the image provider and content.](/images/com.apple.clockkit/media-3667405@2x.png)

The following table lists the dimensions of the SwiftUI view displayed by the template.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 28 points | 14 points |
| 44 mm | 31 points | 16 points |

## Topics

### Creating the Template
- [init(content: Content, textProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularstackviewtext/init(content:textprovider:).md)
  Creates a template that has a view and a small amount of text.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphiccircularstackviewtext/content.md)
  The SwiftUI view displayed by the template.
- [var textProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularstackviewtext/textprovider.md)
  The text to display below the view.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphiccircular.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstackviewtext)*