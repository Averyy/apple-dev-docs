# CLKComplicationTemplateExtraLargeRingText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text encircled by a configurable progress ring.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class CLKComplicationTemplateExtraLargeRingText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.extraLarge`](clkcomplicationfamily/extralarge.md) family.

![A diagram showing the layout of the extra large ring text complication. The diagram shows text inside a progress ring.](/images/com.apple.clockkit/media-2880719@2x.png)

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](clkcomplicationtemplateextralargeringtext/init(textprovider:fillfraction:ringstyle:).md)
  Creates a new template from the provided text, fill fraction, and ring style.
### Setting the Complication Data
- [var fillFraction: Float](clkcomplicationtemplateextralargeringtext/fillfraction.md)
  Setting the Complication Data.
- [var ringStyle: CLKComplicationRingStyle](clkcomplicationtemplateextralargeringtext/ringstyle.md)
  The style of the progress ring.
- [var textProvider: CLKTextProvider](clkcomplicationtemplateextralargeringtext/textprovider.md)
  The text to display in the complication.

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

- [class CLKComplicationTemplateExtraLargeColumnsText](clkcomplicationtemplateextralargecolumnstext.md)
  A template for displaying two rows and two columns of text.
- [class CLKComplicationTemplateExtraLargeSimpleText](clkcomplicationtemplateextralargesimpletext.md)
  A template for displaying a small amount of text.
- [class CLKComplicationTemplateExtraLargeStackText](clkcomplicationtemplateextralargestacktext.md)
  A template for displaying two strings stacked one on top of the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext)*