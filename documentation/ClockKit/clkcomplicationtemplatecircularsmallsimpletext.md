# CLKComplicationTemplateCircularSmallSimpleText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a short text string.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateCircularSmallSimpleText
```

```objc
@interface CLKComplicationTemplateCircularSmallSimpleText : CLKComplicationTemplate
```

## Overview

This template belongs to the circularSmall family.

![A diagram showing the layout of the circular small simple text complication. The diagram shows three examples, each with a single line of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933738@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider)](./clkcomplicationtemplatecircularsmallsimpletext/init%28textprovider%29.md)
  Creates a new template from the provided text.
- [+ templateWithTextProvider:](./clkcomplicationtemplatecircularsmallsimpletext/templatewithtextprovider_.md)
  Returns a new template from the provided text.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](./clkcomplicationtemplatecircularsmallsimpletext/textprovider.md)
  The text to display in the complication.

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
- [class CLKComplicationTemplateCircularSmallStackText](./clkcomplicationtemplatecircularsmallstacktext.md)
  A template for displaying two text strings stacked on top of each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallsimpletext)*