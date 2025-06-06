# Calendar.RecurrenceRule

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct RecurrenceRule
```

## Topics

### Type Aliases
- [Calendar.RecurrenceRule.Specification](calendar/recurrencerule/specification.md)
- [Calendar.RecurrenceRule.UnwrappedType](calendar/recurrencerule/unwrappedtype.md)
- [Calendar.RecurrenceRule.ValueType](calendar/recurrencerule/valuetype.md)
### Initializers
- [init(calendar: Calendar, frequency: Calendar.RecurrenceRule.Frequency, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weeks: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int])](calendar/recurrencerule/init(calendar:frequency:interval:end:matchingpolicy:repeatedtimepolicy:months:daysoftheyear:daysofthemonth:weeks:weekdays:hours:minutes:seconds:setpositions:).md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](calendar/recurrencerule/defaultresolverspecification.md)
### Structures
- [Calendar.RecurrenceRule.End](calendar/recurrencerule/end-swift.struct.md)
- [Calendar.RecurrenceRule.Month](calendar/recurrencerule/month.md)
### Instance Properties
- [var calendar: Calendar](calendar/recurrencerule/calendar.md)
- [var daysOfTheMonth: [Int]](calendar/recurrencerule/daysofthemonth.md)
- [var daysOfTheYear: [Int]](calendar/recurrencerule/daysoftheyear.md)
- [var end: Calendar.RecurrenceRule.End](calendar/recurrencerule/end-swift.property.md)
- [var frequency: Calendar.RecurrenceRule.Frequency](calendar/recurrencerule/frequency-swift.property.md)
- [var hours: [Int]](calendar/recurrencerule/hours.md)
- [var interval: Int](calendar/recurrencerule/interval.md)
- [var matchingPolicy: Calendar.MatchingPolicy](calendar/recurrencerule/matchingpolicy.md)
- [var minutes: [Int]](calendar/recurrencerule/minutes.md)
- [var months: [Calendar.RecurrenceRule.Month]](calendar/recurrencerule/months.md)
- [var repeatedTimePolicy: Calendar.RepeatedTimePolicy](calendar/recurrencerule/repeatedtimepolicy.md)
- [var seconds: [Int]](calendar/recurrencerule/seconds.md)
- [var setPositions: [Int]](calendar/recurrencerule/setpositions.md)
- [var weekdays: [Calendar.RecurrenceRule.Weekday]](calendar/recurrencerule/weekdays.md)
- [var weeks: [Int]](calendar/recurrencerule/weeks.md)
### Instance Methods
- [func recurrences(of: Date, in: Range<Date>?) -> some Sendable & Sequence<Date>
](calendar/recurrencerule/recurrences(of:in:).md)
### Type Methods
- [static func daily(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/daily(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:).md)
- [static func hourly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/hourly(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysoftheyear:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:).md)
- [static func minutely(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/minutely(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysoftheyear:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:).md)
- [static func monthly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/monthly(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysofthemonth:weekdays:hours:minutes:seconds:setpositions:).md)
- [static func weekly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/weekly(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:weekdays:hours:minutes:seconds:setpositions:).md)
- [static func yearly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weeks: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](calendar/recurrencerule/yearly(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysoftheyear:daysofthemonth:weeks:weekdays:hours:minutes:seconds:setpositions:).md)
### Enumerations
- [Calendar.RecurrenceRule.Frequency](calendar/recurrencerule/frequency-swift.enum.md)
- [Calendar.RecurrenceRule.Weekday](calendar/recurrencerule/weekday.md)
### Default Implementations
- [Equatable Implementations](calendar/recurrencerule/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule)*