# CLKComplicationTemplateCircularSmallStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two text strings stacked on top of each other.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateCircularSmallStackText
```

```objc
@interface CLKComplicationTemplateCircularSmallStackText : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](./clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of the circular small stack text complication. The diagram has two examples, each showing two small rows of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933743@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplatecircularsmallstacktext/init%28line1textprovider,line2textprovider%29.md)
  Creates a new template that has two lines of text.
- [+ templateWithLine1TextProvider:line2TextProvider:](./clkcomplicationtemplatecircularsmallstacktext/templatewithline1textprovider_line2textprovider_.md)
  Returns a new template that has two lines of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](./clkcomplicationtemplatecircularsmallstacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplatecircularsmallstacktext/line2textprovider.md)
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
- [class CLKComplicationTemplateCircularSmallRingText](./clkcomplicationtemplatecircularsmallringtext.md)
  A template for displaying a short text string encircled by a configurable progress ring.
- [class CLKComplicationTemplateCircularSmallSimpleText](./clkcomplicationtemplatecircularsmallsimpletext.md)
  A template for displaying a short text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstacktext)*