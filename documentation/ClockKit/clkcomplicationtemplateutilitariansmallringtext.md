# CLKComplicationTemplateUtilitarianSmallRingText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateUtilitarianSmallRingText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.utilitarianSmall`](clkcomplicationfamily/utilitariansmall.md) family.

![A diagram showing the layout of the utilitarian small ring text complication. The diagram shows text inside a small progress ring.](https://docs-assets.developer.apple.com/published/23016f5c798812864149cd40e009b32c/media-2933761%402x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplateutilitariansmallringtext/init(textprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](clkcomplicationtemplateutilitariansmallringtext/textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplateutilitariansmallringtext/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplateutilitariansmallringtext/fillfraction.md)
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

- [class CLKComplicationTemplateUtilitarianSmallFlat](clkcomplicationtemplateutilitariansmallflat.md)
  A template for displaying an image and text in a single line.
- [class CLKComplicationTemplateUtilitarianSmallRingImage](clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallSquare](clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringtext)*