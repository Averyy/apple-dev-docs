# CLKComplicationTemplateModularSmallSimpleText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a small amount of text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularSmallSimpleText
```

```objc
@interface CLKComplicationTemplateModularSmallSimpleText : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](./clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small simple text complication. The diagram shows a small amount of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933756@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider)](./clkcomplicationtemplatemodularsmallsimpletext/init%28textprovider%29.md)
  Creates a new template from the provided text.
- [+ templateWithTextProvider:](./clkcomplicationtemplatemodularsmallsimpletext/templatewithtextprovider_.md)
  Returns a new template from the provided text.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](./clkcomplicationtemplatemodularsmallsimpletext/textprovider.md)
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
- [class CLKComplicationTemplateModularSmallColumnsText](./clkcomplicationtemplatemodularsmallcolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateModularSmallRingText](./clkcomplicationtemplatemodularsmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateModularSmallStackText](./clkcomplicationtemplatemodularsmallstacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallsimpletext)*