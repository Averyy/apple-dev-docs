# CLKComplicationTemplateExtraLargeStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two strings stacked one on top of the other.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large stack text complication. The diagram shows two rows of text.](https://docs-assets.developer.apple.com/published/6c5107a7fb743c451016593bfc6e9cba/media-2880724%402x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplateextralargestacktext/init(line1textprovider:line2textprovider:).md)
  Creates a new template that has two rows of text.
### Setting the Complication Data
- [var highlightLine2: Bool](clkcomplicationtemplateextralargestacktext/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.
- [var line1TextProvider: CLKTextProvider](clkcomplicationtemplateextralargestacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplateextralargestacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.

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

- [class CLKComplicationTemplateExtraLargeColumnsText](clkcomplicationtemplateextralargecolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateExtraLargeRingText](clkcomplicationtemplateextralargeringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateExtraLargeSimpleText](clkcomplicationtemplateextralargesimpletext.md)
  A template for displaying a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext)*