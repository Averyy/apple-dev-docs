# CLKComplicationTemplateGraphicExtraLargeCircularStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two rows of text in an extra-large, circular complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularstacktext#3667233.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the text providers.](/images/com.apple.clockkit/media-3667233@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularstacktext/init(line1textprovider:line2textprovider:).md)
  Creates a new template with two rows of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularstacktext/line1textprovider.md)
  The text to display on the top row.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularstacktext/line2textprovider.md)
  The text to display on the bottom row.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateGraphicExtraLargeCircularImage](clkcomplicationtemplategraphicextralargecircularimage.md)
  A template for displaying an extra-large, full-color circular image.
- [class CLKComplicationTemplateGraphicExtraLargeCircularView](clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackImage](clkcomplicationtemplategraphicextralargecircularstackimage.md)
  A template for displaying an extra-large, full-color circular image and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstacktext)*