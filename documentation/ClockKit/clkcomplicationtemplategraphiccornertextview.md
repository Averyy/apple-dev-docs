# CLKComplicationTemplateGraphicCornerTextView

**Framework**: ClockKit  
**Kind**: class

A template for displaying a SwiftUI view and text in the clock face’s corner.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
final class CLKComplicationTemplateGraphicCornerTextView<Label> where Label : View
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the view and where the template might appear on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the text provider and label.](https://docs-assets.developer.apple.com/published/4e2c10da3f546dc9dc9cf8c10ca61efb/media-3667263%402x.png)

The following table lists the dimensions of the view displayed by the template. The template masks the view to a circle.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 20 points | 20 points |
| 41 mm | 21 points | 21 points |
| 44 mm | 22 points | 22 points |
| 45 mm | 24 points | 24 points |

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, label: Label)](clkcomplicationtemplategraphiccornertextview/init(textprovider:label:).md)
  Creates a template with a line of text and a SwiftUI view.
### Accessing the Content
- [var textProvider: CLKTextProvider](clkcomplicationtemplategraphiccornertextview/textprovider.md)
  The text provider for the text.
- [var label: Label](clkcomplicationtemplategraphiccornertextview/label.md)
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

- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextview)*