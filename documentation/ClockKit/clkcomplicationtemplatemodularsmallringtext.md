# CLKComplicationTemplateModularSmallRingText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularSmallRingText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularSmall`](clkcomplicationfamily/modularsmall.md) family.

![A diagram showing the layout of the modular small ring text complication. The diagram shows text inside a small progress ring.](https://docs-assets.developer.apple.com/published/c4a5ba0d520030a0d1b3fbe8afba3624/media-2933755%402x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplatemodularsmallringtext/init(textprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](clkcomplicationtemplatemodularsmallringtext/textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplatemodularsmallringtext/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplatemodularsmallringtext/fillfraction.md)
  The fraction of the ring to fill.

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

- [class CLKComplicationTemplateModularSmallColumnsText](clkcomplicationtemplatemodularsmallcolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateModularSmallSimpleText](clkcomplicationtemplatemodularsmallsimpletext.md)
  A template for displaying a small amount of text.
- [class CLKComplicationTemplateModularSmallStackText](clkcomplicationtemplatemodularsmallstacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringtext)*