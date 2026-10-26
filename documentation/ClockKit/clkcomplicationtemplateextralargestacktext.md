# CLKComplicationTemplateExtraLargeStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two strings stacked one on top of the other.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateExtraLargeStackText
```

```objc
@interface CLKComplicationTemplateExtraLargeStackText : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](./clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large stack text complication. The diagram shows two rows of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2880724@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplateextralargestacktext/init%28line1textprovider,line2textprovider%29.md)
  Creates a new template that has two rows of text.
- [+ templateWithLine1TextProvider:line2TextProvider:](./clkcomplicationtemplateextralargestacktext/templatewithline1textprovider_line2textprovider_.md)
  Returns a new template that has two rows of text.
### Setting the Complication Data
- [var highlightLine2: Bool](./clkcomplicationtemplateextralargestacktext/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.
- [var line1TextProvider: CLKTextProvider](./clkcomplicationtemplateextralargestacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplateextralargestacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.

## Relationships

### Inherits From
- [CLKComplicationTemplate](./clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text templates
- [class CLKComplicationTemplateExtraLargeColumnsText](./clkcomplicationtemplateextralargecolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateExtraLargeRingText](./clkcomplicationtemplateextralargeringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateExtraLargeSimpleText](./clkcomplicationtemplateextralargesimpletext.md)
  A template for displaying a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext)*