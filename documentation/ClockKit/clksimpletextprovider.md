# CLKSimpleTextProvider

**Framework**: ClockKit  
**Kind**: class

A single line of text to display in your complication interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKSimpleTextProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

Use a simple text provider to specify strings for your complications. The simple text object handles the formatting of that string in your complication, which may include tinting it to match the color of the clock face.

When creating a simple text provider, you can specify both a long version and a short version of your text. Providing both strings gives you more control over the text displayed by your complication. When the long string doesn’t fit in the available space, the text provider tries to display the value in the [`shortText`](clksimpletextprovider/shorttext.md) property instead. If the shorter version is still too long, it displays a truncated version of the longer text.

## Topics

### Creating a Text Provider
- [convenience init(text: String)](clksimpletextprovider/init(text:).md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?)](clksimpletextprovider/init(text:shorttext:).md)
  Creates and returns a text provider with both long and short versions of the text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](clksimpletextprovider/init(text:shorttext:accessibilitylabel:).md)
  Creates and returns a text provider with the text strings and an accessible string.
### Getting the Text
- [var text: String](clksimpletextprovider/text.md)
  The long version of text that you want to display.
- [var shortText: String?](clksimpletextprovider/shorttext.md)
  A shorter version of the text.

## Relationships

### Inherits From
- [CLKTextProvider](clktextprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKDateTextProvider](clkdatetextprovider.md)
  A formatted string that conveys a date without any time information.
- [class CLKRelativeDateTextProvider](clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeIntervalTextProvider](clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider)*