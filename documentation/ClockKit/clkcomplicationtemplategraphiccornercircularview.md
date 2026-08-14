# CLKComplicationTemplateGraphicCornerCircularView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view in the clock face’s corner.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCornerCircularView<Content> where Content : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family. [`Figure 1`](clkcomplicationtemplategraphiccornercircularview#3667248.md) shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content.](/images/com.apple.clockkit/media-3667248@2x.png)

The following table lists the dimensions of the SwiftUI view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 32 points | 32 points |
| 41 mm | 34 points | 34 points |
| 44 mm | 36 points | 36 points |
| 45 mm | 38 points | 38 points |

## Topics

### Creating the Template
- [init(Content)](clkcomplicationtemplategraphiccornercircularview/init(_:).md)
  Creates a template that has a circular SwiftUI view.
### Accessing the Content
- [var content: Content](clkcomplicationtemplategraphiccornercircularview/content.md)
  The SwiftUI view displayed by the template.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornercircularview)*