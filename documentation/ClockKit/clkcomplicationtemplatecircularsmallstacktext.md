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

![A diagram showing the layout of the circular small stack text complication. The diagram has two examples, each showing two small rows of text.](https://docs-assets.developer.apple.com/published/c65d0106f8b763df0c4843c10f46047a/media-2933743%402x.png)

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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateCircularSmallRingText](clkcomplicationtemplatecircularsmallringtext.md)
  A template for displaying a short text string encircled by a configurable progress ring.
- [class CLKComplicationTemplateCircularSmallSimpleText](clkcomplicationtemplatecircularsmallsimpletext.md)
  A template for displaying a short text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstacktext)*