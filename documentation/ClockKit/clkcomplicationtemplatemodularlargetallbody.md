# CLKComplicationTemplateModularLargeTallBody

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a header row and row of tall body text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularLargeTallBody
```

```objc
@interface CLKComplicationTemplateModularLargeTallBody : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](./clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large tall body complication. The diagram shows  the header row above a single line of large body text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933748@2x.png)

## Topics

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, bodyTextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularlargetallbody/init%28headertextprovider,bodytextprovider%29.md)
  Creates a template that has a header and a row of tall body text.
- [+ templateWithHeaderTextProvider:bodyTextProvider:](./clkcomplicationtemplatemodularlargetallbody/templatewithheadertextprovider_bodytextprovider_.md)
  Returns a template that has a header and a row of tall body text.
### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](./clkcomplicationtemplatemodularlargetallbody/headertextprovider.md)
  The text to display in the header line.
- [var bodyTextProvider: CLKTextProvider](./clkcomplicationtemplatemodularlargetallbody/bodytextprovider.md)
  The text to display in the body line.

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

### Body templates
- [class CLKComplicationTemplateModularLargeStandardBody](./clkcomplicationtemplatemodularlargestandardbody.md)
  A template for displaying a header row and two lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody)*