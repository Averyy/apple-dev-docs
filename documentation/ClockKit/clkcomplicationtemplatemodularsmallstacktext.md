# CLKComplicationTemplateModularSmallStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two strings stacked one on top of the other.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularSmallStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small stack text complication. The diagram shows two small rows of text.](https://docs-assets.developer.apple.com/published/04b07ee296113e69756cd4ec610841ec/media-2933757%402x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularsmallstacktext/init(line1textprovider:line2textprovider:).md)
  Creates a new template that has two lines of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallstacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallstacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.
- [var highlightLine2: Bool](clkcomplicationtemplatemodularsmallstacktext/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.

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

- [class CLKComplicationTemplateModularSmallColumnsText](clkcomplicationtemplatemodularsmallcolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateModularSmallRingText](clkcomplicationtemplatemodularsmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallSimpleText](clkcomplicationtemplatemodularsmallsimpletext.md)
  A template for displaying a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstacktext)*