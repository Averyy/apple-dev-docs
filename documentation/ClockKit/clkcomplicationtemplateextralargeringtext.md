# CLKComplicationTemplateExtraLargeRingText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying text encircled by a configurable progress ring.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateExtraLargeRingText
```

```objc
@interface CLKComplicationTemplateExtraLargeRingText : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](./clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large ring text complication. The diagram shows text inside a progress ring.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2880719@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./clkcomplicationtemplateextralargeringtext/init%28textprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided text, fill fraction, and ring style.
- [+ templateWithTextProvider:fillFraction:ringStyle:](./clkcomplicationtemplateextralargeringtext/templatewithtextprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var fillFraction: Float](./clkcomplicationtemplateextralargeringtext/fillfraction.md)
  Setting the Complication Data.
- [var ringStyle: CLKComplicationRingStyle](./clkcomplicationtemplateextralargeringtext/ringstyle.md)
  The style of the progress ring.
- [var textProvider: CLKTextProvider](./clkcomplicationtemplateextralargeringtext/textprovider.md)
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
- [class CLKComplicationTemplateExtraLargeColumnsText](./clkcomplicationtemplateextralargecolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateExtraLargeSimpleText](./clkcomplicationtemplateextralargesimpletext.md)
  A template for displaying a small amount of text.
- [class CLKComplicationTemplateExtraLargeStackText](./clkcomplicationtemplateextralargestacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext)*