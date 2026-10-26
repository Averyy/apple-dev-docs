# CLKComplicationTemplateUtilitarianSmallRingText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying text encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallRingText
```

```objc
@interface CLKComplicationTemplateUtilitarianSmallRingText : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](./clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small ring text complication. The diagram shows text inside a small progress ring.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933761@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./clkcomplicationtemplateutilitariansmallringtext/init%28textprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided text, fill fraction, and ring style.
- [+ templateWithTextProvider:fillFraction:ringStyle:](./clkcomplicationtemplateutilitariansmallringtext/templatewithtextprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](./clkcomplicationtemplateutilitariansmallringtext/textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](./clkcomplicationtemplateutilitariansmallringtext/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](./clkcomplicationtemplateutilitariansmallringtext/fillfraction.md)
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

### Utilitarian small
- [class CLKComplicationTemplateUtilitarianSmallFlat](./clkcomplicationtemplateutilitariansmallflat.md)
  A template for displaying an image and text in a single line.
- [class CLKComplicationTemplateUtilitarianSmallRingImage](./clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallSquare](./clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringtext)*