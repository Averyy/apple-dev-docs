# CLKComplicationTemplateCircularSmallRingText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a short text string encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateCircularSmallRingText
```

```objc
@interface CLKComplicationTemplateCircularSmallRingText : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](./clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of the circular small ring text complication. The diagram shows three examples, each displaying text inside a small progress ring.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933737@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./clkcomplicationtemplatecircularsmallringtext/init%28textprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided text, fill fraction, and ring style.
- [+ templateWithTextProvider:fillFraction:ringStyle:](./clkcomplicationtemplatecircularsmallringtext/templatewithtextprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](./clkcomplicationtemplatecircularsmallringtext/textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](./clkcomplicationtemplatecircularsmallringtext/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](./clkcomplicationtemplatecircularsmallringtext/fillfraction.md)
  The fraction of the ring to fill.

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
- [class CLKComplicationTemplateCircularSmallSimpleText](./clkcomplicationtemplatecircularsmallsimpletext.md)
  A template for displaying a short text string.
- [class CLKComplicationTemplateCircularSmallStackText](./clkcomplicationtemplatecircularsmallstacktext.md)
  A template for displaying two text strings stacked on top of each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringtext)*