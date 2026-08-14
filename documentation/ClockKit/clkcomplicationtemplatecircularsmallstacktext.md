# CLKComplicationTemplateCircularSmallStackText

**Framework**: ClockKit  
**Kind**: class

A template for displaying two text strings stacked on top of each other.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplateCircularSmallStackText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.circularSmall`](clkcomplicationfamily/circularsmall.md) family.

![A diagram showing the layout of the circular small stack text complication. The diagram has two examples, each showing two small rows of text.](/images/com.apple.clockkit/media-2933743@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplatecircularsmallstacktext/init(line1textprovider:line2textprovider:).md)
  Creates a new template that has two lines of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](clkcomplicationtemplatecircularsmallstacktext/line1textprovider.md)
  The text to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplatecircularsmallstacktext/line2textprovider.md)
  The text to display on the bottom line of the complication.

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

- [class CLKComplicationTemplateCircularSmallRingText](clkcomplicationtemplatecircularsmallringtext.md)
  A template for displaying a short text string encircled by a configurable progress ring.
- [class CLKComplicationTemplateCircularSmallSimpleText](clkcomplicationtemplatecircularsmallsimpletext.md)
  A template for displaying a short text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstacktext)*