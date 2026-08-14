# CLKComplicationTemplateModularLargeTallBody

**Framework**: ClockKit  
**Kind**: class

A template for displaying a header row and row of tall body text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateModularLargeTallBody
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large tall body complication. The diagram shows  the header row above a single line of large body text.](/images/com.apple.clockkit/media-2933748@2x.png)

## Topics

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, bodyTextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargetallbody/init(headertextprovider:bodytextprovider:).md)
  Creates a template that has a header and a row of tall body text.
### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetallbody/headertextprovider.md)
  The text to display in the header line.
- [var bodyTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetallbody/bodytextprovider.md)
  The text to display in the body line.

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

- [class CLKComplicationTemplateModularLargeStandardBody](clkcomplicationtemplatemodularlargestandardbody.md)
  A template for displaying a header row and two lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody)*