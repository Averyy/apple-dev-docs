# Calendar.RecurrenceRule

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A rule which specifies how often an event should repeat in the future

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
- [Calendar.RecurrenceRule.Specification](./recurrencerule/specification.md)
- [Calendar.RecurrenceRule.UnwrappedType](./recurrencerule/unwrappedtype.md)
- [Calendar.RecurrenceRule.ValueType](./recurrencerule/valuetype.md)
### Initializers
- [init(calendar: Calendar, frequency: Calendar.RecurrenceRule.Frequency, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weeks: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int])](./recurrencerule/init%28calendar,frequency,interval,end,matchingpolicy,repeatedtimepolicy,months,daysoftheyear,daysofthemonth,weeks,weekdays,hours,minutes,seconds,setpositions%29.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](./recurrencerule/defaultresolverspecification.md)
### Structures
- [Calendar.RecurrenceRule.End](./recurrencerule/end-swift.struct.md)
  When a recurring event stops recurring.
- [Calendar.RecurrenceRule.Month](./recurrencerule/month.md)
  Uniquely identifies a month in any calendar system.
### Instance Properties
- [var calendar: Calendar](./recurrencerule/calendar.md)
  The calendar in which the recurrence occurs
- [var daysOfTheMonth: [Int]](./recurrencerule/daysofthemonth.md)
  On which days in the month the event should occur
- [var daysOfTheYear: [Int]](./recurrencerule/daysoftheyear.md)
  On which days of the year the event may occur.
- [var end: Calendar.RecurrenceRule.End](./recurrencerule/end-swift.property.md)
  For how long the event repeats
- [var frequency: Calendar.RecurrenceRule.Frequency](./recurrencerule/frequency-swift.property.md)
  How often the event repeats
- [var hours: [Int]](./recurrencerule/hours.md)
  On which hours of a 24-hour day the event should repeat.
- [var interval: Int](./recurrencerule/interval.md)
  At what interval to repeat
- [var matchingPolicy: Calendar.MatchingPolicy](./recurrencerule/matchingpolicy.md)
  What to do when a recurrence is not a valid date
- [var minutes: [Int]](./recurrencerule/minutes.md)
  On which minutes of the hour the event should repeat. Accepts values between 0 and 59
- [var months: [Calendar.RecurrenceRule.Month]](./recurrencerule/months.md)
  On which months the event should occur.
- [var repeatedTimePolicy: Calendar.RepeatedTimePolicy](./recurrencerule/repeatedtimepolicy.md)
  What to do when there are multiple recurrences occurring at the same time of the day but in different time zones due to a daylight saving transition.
- [var seconds: [Int]](./recurrencerule/seconds.md)
  On which seconds of the minute the event should repeat. Valid values between 0 and 60
- [var setPositions: [Int]](./recurrencerule/setpositions.md)
  Which occurrences within every interval should be returned
- [var weekdays: [Calendar.RecurrenceRule.Weekday]](./recurrencerule/weekdays.md)
  On which days of the week the event should occur
- [var weeks: [Int]](./recurrencerule/weeks.md)
  On which weeks of the year the event should occur.
### Instance Methods
- [func recurrences(of: Date, in: Range<Date>?) -> some Sendable & Sequence<Date>
](./recurrencerule/recurrences%28of,in%29-4y30t.md)
  Find recurrences of the given date
- [func recurrences(of: Date, in: PartialRangeUpTo<Date>) -> some Sendable & Sequence<Date>
](./recurrencerule/recurrences%28of,in%29-7b1ww.md)
  Find recurrences of the given date
- [func recurrences(of: Date, in: ClosedRange<Date>) -> some Sendable & Sequence<Date>
](./recurrencerule/recurrences%28of,in%29-7k3ha.md)
  Find recurrences of the given date
- [func recurrences(of: Date, in: PartialRangeFrom<Date>) -> some Sendable & Sequence<Date>
](./recurrencerule/recurrences%28of,in%29-8l967.md)
  Find recurrences of the given date
- [func recurrences(of: Date, in: PartialRangeThrough<Date>) -> some Sendable & Sequence<Date>
](./recurrencerule/recurrences%28of,in%29-9qfbm.md)
  Find recurrences of the given date
### Type Methods
- [static func daily(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/daily%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,daysofthemonth,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` days
- [static func hourly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/hourly%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,daysoftheyear,daysofthemonth,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` hours
- [static func minutely(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/minutely%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,daysoftheyear,daysofthemonth,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` minutes
- [static func monthly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheMonth: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/monthly%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,daysofthemonth,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` months
- [static func weekly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/weekly%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` weeks
- [static func yearly(calendar: Calendar, interval: Int, end: Calendar.RecurrenceRule.End, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, months: [Calendar.RecurrenceRule.Month], daysOfTheYear: [Int], daysOfTheMonth: [Int], weeks: [Int], weekdays: [Calendar.RecurrenceRule.Weekday], hours: [Int], minutes: [Int], seconds: [Int], setPositions: [Int]) -> Calendar.RecurrenceRule](./recurrencerule/yearly%28calendar,interval,end,matchingpolicy,repeatedtimepolicy,months,daysoftheyear,daysofthemonth,weeks,weekdays,hours,minutes,seconds,setpositions%29.md)
  A recurrence that repeats every `interval` years
### Enumerations
- [Calendar.RecurrenceRule.Frequency](./recurrencerule/frequency-swift.enum.md)
  How often a recurring event repeats
- [Calendar.RecurrenceRule.Weekday](./recurrencerule/weekday.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [IntentValueConvertible](../../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../../AppIntents/intentvalueexpressing.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule)*