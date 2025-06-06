# CLKComplicationTemplateGraphicCornerStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying stacked text in the clock face’s corner.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of the outer and inner text.](https://docs-assets.developer.apple.com/published/e4f82129b55b2d9a2d4d7e333dec8b0e/media-3030692%402x.png)

The system always displays the outer text as white. The inner text can be multicolored.

## Topics

### Creating the Template
- [init(innerTextProvider: CLKTextProvider, outerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccornerstacktext/init(innertextprovider:outertextprovider:).md)
  Creates a template that has an inner line of text and an outer text element.
### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccornerstacktext/outertextprovider.md)
  The outer text to display in the complication.
- [var innerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccornerstacktext/innertextprovider.md)
  The inner text to display in the complication.

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

- [class CLKComplicationTemplateGraphicCornerCircularImage](clkcomplicationtemplategraphiccornercircularimage.md)
  A template for displaying an image in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextImage](clkcomplicationtemplategraphiccornertextimage.md)
  A template for displaying an image and text in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext)*