# CLKSimpleTextProvider

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A single line of text to display in your complication interface.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKSimpleTextProvider
```

```objc
@interface CLKSimpleTextProvider : CLKTextProvider
```

## Mentions

- [Creating a timeline entry](./creating-a-timeline-entry.md)

#### Overview

Use a simple text provider to specify strings for your complications. The simple text object handles the formatting of that string in your complication, which may include tinting it to match the color of the clock face.

When creating a simple text provider, you can specify both a long version and a short version of your text. Providing both strings gives you more control over the text displayed by your complication. When the long string doesn’t fit in the available space, the text provider tries to display the value in the [`shortText`](./clksimpletextprovider/shorttext.md) property instead. If the shorter version is still too long, it displays a truncated version of the longer text.

## Topics

### Creating a Text Provider
- [convenience init(text: String)](./clksimpletextprovider/init%28text%29.md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?)](./clksimpletextprovider/init%28text,shorttext%29.md)
  Creates and returns a text provider with both long and short versions of the text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](./clksimpletextprovider/init%28text,shorttext,accessibilitylabel%29.md)
  Creates and returns a text provider with the text strings and an accessible string.
### Getting the Text
- [var text: String](./clksimpletextprovider/text.md)
  The long version of text that you want to display.
- [var shortText: String?](./clksimpletextprovider/shorttext.md)
  A shorter version of the text.

## Relationships

### Inherits From
- [CLKTextProvider](./clktextprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text providers
- [class CLKDateTextProvider](./clkdatetextprovider.md)
  A formatted string that conveys a date without any time information.
- [class CLKRelativeDateTextProvider](./clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeIntervalTextProvider](./clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](./clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](./clktextprovider.md)
  The common behavior for displaying text-based data in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider)*