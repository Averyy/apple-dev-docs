# CLKComplicationTemplateCircularSmallRingText

**Framework**: ClockKit  
**Kind**: class

A template for displaying a short text string encircled by a configurable progress ring.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateCircularSmallRingText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of the circular small ring text complication. The diagram shows three examples, each displaying text inside a small progress ring.](/images/com.apple.clockkit/media-2933737@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplatecircularsmallringtext/init(textprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](clkcomplicationtemplatecircularsmallringtext/textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplatecircularsmallringtext/ringstyle.md)
  The style of the progress ring.
- [var fillFraction: Float](clkcomplicationtemplatecircularsmallringtext/fillfraction.md)
  The fraction of the ring to fill.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CLKComplicationTemplateCircularSmallSimpleText](clkcomplicationtemplatecircularsmallsimpletext.md)
  A template for displaying a short text string.
- [class CLKComplicationTemplateCircularSmallStackText](clkcomplicationtemplatecircularsmallstacktext.md)
  A template for displaying two text strings stacked on top of each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringtext)*