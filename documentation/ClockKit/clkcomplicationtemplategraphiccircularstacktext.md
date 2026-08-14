# CLKComplicationTemplateGraphicCircularStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two rows of text.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family.

![Diagram showing the layout of a circular template containing two rows of text.](/images/com.apple.clockkit/media-3262158@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularstacktext/init(line1textprovider:line2textprovider:).md)
  Creates a new template that has two small rows of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularstacktext/line1textprovider.md)
  The text to display on the top row.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularstacktext/line2textprovider.md)
  The text to display on the bottom row.

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

- [class CLKComplicationTemplateGraphicCircularImage](clkcomplicationtemplategraphiccircularimage.md)
  A template for displaying a full-color circular image.
- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularStackImage](clkcomplicationtemplategraphiccircularstackimage.md)
  A template for displaying a full-color circular image and text.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstacktext)*