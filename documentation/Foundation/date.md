# Date

**Framework**: Foundation  
**Kind**: struct

A specific point in time, independent of any calendar or time zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Date
```

## Mentions

- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)

#### Overview

A [`Date`](date.md) value encapsulate a single point in time, independent of any particular calendrical system or time zone. Date values represent a time interval relative to an absolute reference date.

The [`Date`](date.md) structure provides methods for comparing dates, calculating the time interval between two dates, and creating a new date from a time interval relative to another date. Use date values in conjunction with [`DateFormatter`](dateformatter.md) instances to create localized representations of dates and times and with [`Calendar`](calendar.md) instances to perform calendar arithmetic.

[`Date`](date.md) bridges to the [`NSDate`](nsdate.md) class. You can use these interchangeably in code that interacts with Objective-C APIs.

## Topics

### Creating a Date
- [init()](date/init.md)
  Creates a date value initialized to the current date and time.
- [init(timeIntervalSinceNow: TimeInterval)](date/init(timeintervalsincenow:).md)
  Creates a date value initialized relative to the current date and time by a given number of seconds.
- [init(timeInterval: TimeInterval, since: Date)](date/init(timeinterval:since:).md)
  Creates a date value initialized relative to another given date by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](date/init(timeintervalsincereferencedate:).md)
  Creates a date value initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [init(timeIntervalSince1970: TimeInterval)](date/init(timeintervalsince1970:).md)
  Creates a date value initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
### Retrieving the Current Date
- [static var now: Date](date/now.md)
  Returns a date instance that represents the current date and time, at the moment of access.
### Getting Temporal Boundaries
- [static let distantFuture: Date](date/distantfuture.md)
  A date value representing a date in the distant future.
- [static let distantPast: Date](date/distantpast.md)
  A date value representing a date in the distant past.
### Comparing Dates
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func > (Date, Date) -> Bool](date/_(_:_:)-880ns.md)
  Returns true if the left hand `Date` is later in time than the right hand `Date`.
- [static func >= (Self, Self) -> Bool](date/_=(_:_:)-8n5kd.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func < (Date, Date) -> Bool](date/_(_:_:)-42kro.md)
  Returns true if the left hand `Date` is earlier in time than the right hand `Date`.
- [static func <= (Self, Self) -> Bool](date/_=(_:_:)-2m6jx.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [func compare(Date) -> ComparisonResult](date/compare(_:).md)
  Compares another date to this one.
### Getting Time Intervals
- [func timeIntervalSince(Date) -> TimeInterval](date/timeintervalsince(_:).md)
  Returns the interval between this date and another given date.
- [var timeIntervalSinceNow: TimeInterval](date/timeintervalsincenow.md)
  The time interval between the date value and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](date/timeintervalsincereferencedate-swift.property.md)
  The interval between the date value and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](date/timeintervalsince1970.md)
  The interval between the date value and 00:00:00 UTC on 1 January 1970.
- [static var timeIntervalSinceReferenceDate: TimeInterval](date/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [static let timeIntervalBetween1970AndReferenceDate: Double](date/timeintervalbetween1970andreferencedate.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.
### Adding or Subtracting a Time Interval
- [func addTimeInterval(TimeInterval)](date/addtimeinterval(_:).md)
  Adds a time interval to this date.
- [func addingTimeInterval(TimeInterval) -> Date](date/addingtimeinterval(_:).md)
  Creates a new date value by adding a time interval to this date.
- [static func + (Date, TimeInterval) -> Date](date/+(_:_:).md)
  Returns a date with a specified amount of time added to it.
- [static func += (inout Date, TimeInterval)](date/+=(_:_:).md)
  Adds a time interval to a date.
- [static func - (Date, TimeInterval) -> Date](date/-(_:_:).md)
  Returns a `Date` with a specified amount of time subtracted from it.
- [static func -= (inout Date, TimeInterval)](date/-=(_:_:).md)
  Subtract a `TimeInterval` from a `Date`.
### Formatting a Date
- [func formatted() -> String](date/formatted.md)
  Generates a locale-aware string representation of a date using the default date format style.
- [func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String](date/formatted(date:time:).md)
  Generates a locale-aware string representation of a date using specified date and time format styles.
- [func formatted<F>(F) -> F.FormatOutput](date/formatted(_:).md)
  Generates a locale-aware string representation of a date using the specified date format style.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [func ISO8601Format(Date.ISO8601FormatStyle) -> String](date/iso8601format(_:).md)
  Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.
### Creating Date Ranges
- [static func ... (Self) -> PartialRangeFrom<Self>](date/'...(_:)-5kkdg.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](date/'...(_:)-6kfkw.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](date/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self) -> PartialRangeUpTo<Self>](date/'.._(_:).md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ..< (Self, Self) -> Range<Self>](date/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
### Describing Dates
- [var description: String](date/description.md)
  The representation is useful for debugging only. There are a number of options to acquire a formatted string for a date including: date formatters (see [`NSDateFormatter`](https://developer.apple.com//apple_ref/occ/cl/NSDateFormatter) and [`Data Formatting Guide`](https://developer.apple.com//apple_ref/doc/uid/10000029i)), and the `Date` function `description(locale:)`.
- [func description(with: Locale?) -> String](date/description(with:).md)
  Returns a string representation of the receiver using the given locale.
- [var customPlaygroundQuickLook: PlaygroundQuickLook](date/customplaygroundquicklook.md)
  A custom playground Quick Look for the date.
### Using Reference Types
- [class NSDate](nsdate.md)
  A representation of a specific point in time, independent of any calendar or time zone.
### Structures
- [struct AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md)
- [struct AttributedStyle](date/attributedstyle.md)
  A structure that creates a locale-appropriate attributed string representation of a date instance.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [struct FormatString](date/formatstring.md)
- [struct HTTPFormatStyle](date/httpformatstyle.md)
  Options for generating and parsing string representations of dates following the HTTP date format from [`RFC 9110 § 5.6.7`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9110.html#http.date).
- [struct ParseStrategy](date/parsestrategy.md)
- [struct SystemClockDidChangeMessage](date/systemclockdidchangemessage.md)
- [struct VerbatimFormatStyle](date/verbatimformatstyle.md)
  A style that formats a date with an explicitly-specified style.
### Initializers
- [init<T>(T.ParseInput, strategy: T) throws](date/init(_:strategy:)-2oqi.md)
- [init<T, Value>(Value, strategy: T) throws](date/init(_:strategy:)-6cq9s.md)
### Type Aliases
- [typealias Specification](date/specification.md)
- [typealias UnwrappedType](date/unwrappedtype.md)
- [typealias ValueType](date/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](date/defaultresolverspecification.md)
### Default Implementations
- [Comparable Implementations](date/comparable-implementations.md)
- [CustomStringConvertible Implementations](date/customstringconvertible-implementations.md)
- [Equatable Implementations](date/equatable-implementations.md)

## Relationships

### Conforms To
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Strideable](../Swift/Strideable.md)

## See Also

- [struct DateInterval](dateinterval.md)
  The span of time between a specific start date and end date.
- [typealias TimeInterval](timeinterval.md)
  A number of seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date)*