# DateComponentsFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that creates string representations of quantities of time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class DateComponentsFormatter
```

#### Overview

An [`DateComponentsFormatter`](datecomponentsformatter.md) object takes quantities of time and formats them as a user-readable string. Use a date components formatter to create strings for your app’s interface. The formatter object has many options for creating both abbreviated and expanded strings. The formatter takes the current user’s locale and language into account when generating strings.

To use this class, create an instance, configure its properties, and call one of its methods to generate an appropriate string. The properties of this class let you configure the calendar and specify the date and time units you want displayed in the resulting string. The listing below shows how to configure a formatter to create the string “About 5 minutes remaining”.

The methods of this class may be called safely from any thread of your app. It is also safe to share a single instance of this class from multiple threads, with the caveat that you should not change the configuration of the object while another thread is using it to generate a string.

> 💡 **Tip**:  In Swift, you can use [`Date.RelativeFormatStyle`](date/relativeformatstyle.md) rather than [`DateComponentsFormatter`](datecomponentsformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

 In Swift, you can use [`Date.RelativeFormatStyle`](date/relativeformatstyle.md) rather than [`DateComponentsFormatter`](datecomponentsformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Topics

### Formatting Values
- [func string(from: DateComponents) -> String?](datecomponentsformatter/string(from:)-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(for: Any?) -> String?](datecomponentsformatter/string(for:).md)
  Returns a formatted string based on the date information in the specified object.
- [func string(from: Date, to: Date) -> String?](datecomponentsformatter/string(from:to:).md)
  Returns a formatted string based on the time difference between two dates.
- [func string(from: TimeInterval) -> String?](datecomponentsformatter/string(from:)-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](datecomponentsformatter/localizedstring(from:unitsstyle:).md)
  Returns a localized string based on the specified date components and style option.
### Configuring the Formatter Options
- [var allowedUnits: NSCalendar.Unit](datecomponentsformatter/allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](datecomponentsformatter/allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](datecomponentsformatter/calendar.md)
  The default calendar to use when formatting date components.
- [var collapsesLargestUnit: Bool](datecomponentsformatter/collapseslargestunit.md)
  A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [var includesApproximationPhrase: Bool](datecomponentsformatter/includesapproximationphrase.md)
  A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [var includesTimeRemainingPhrase: Bool](datecomponentsformatter/includestimeremainingphrase.md)
  A Boolean value indicating whether output strings reflect the amount of time remaining.
- [var maximumUnitCount: Int](datecomponentsformatter/maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](datecomponentsformatter/unitsstyle-swift.property.md)
  The formatting style for unit names.
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.
### Constants
- [DateComponentsFormatter.UnitsStyle](datecomponentsformatter/unitsstyle-swift.enum.md)
  Constants for specifying how to represent quantities of time.
- [DateComponentsFormatter.ZeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.struct.md)
  Formatting constants for when values contain zeroes.
### Instance Properties
- [var formattingContext: Formatter.Context](datecomponentsformatter/formattingcontext.md)
- [var referenceDate: Date?](datecomponentsformatter/referencedate.md)
### Instance Methods
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](datecomponentsformatter/getobjectvalue(_:for:errordescription:).md)

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class DateFormatter](dateformatter.md)
  A formatter that converts between dates and their textual representations.
- [class RelativeDateTimeFormatter](relativedatetimeformatter.md)
  A formatter that creates locale-aware string representations of a relative date or time.
- [class DateIntervalFormatter](dateintervalformatter.md)
  A formatter that creates string representations of time intervals.
- [class ISO8601DateFormatter](iso8601dateformatter.md)
  A formatter that converts between dates and their ISO 8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter)*