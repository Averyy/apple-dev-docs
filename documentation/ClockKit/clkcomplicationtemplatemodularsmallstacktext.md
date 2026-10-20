# CLKComplicationTemplateModularSmallStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two strings stacked one on top of the other.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularSmallStackText
```

```objc
@interface CLKComplicationTemplateModularSmallStackText : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](./clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small stack text complication. The diagram shows two small rows of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933757@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularsmallstacktext/init%28line1textprovider,line2textprovider%29.md)
  Creates a new template that has two lines of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallstacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallstacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.
- [var highlightLine2: Bool](./clkcomplicationtemplatemodularsmallstacktext/highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.

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
- [class CLKComplicationTemplateModularSmallColumnsText](./clkcomplicationtemplatemodularsmallcolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateModularSmallRingText](./clkcomplicationtemplatemodularsmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallSimpleText](./clkcomplicationtemplatemodularsmallsimpletext.md)
  A template for displaying a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstacktext)*