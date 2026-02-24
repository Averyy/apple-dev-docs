# init(recurrenceWith:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:)

**Framework**: EventKit  
**Kind**: init

Initializes and returns a recurrence rule with a given frequency and additional scheduling information.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(recurrenceWith type: EKRecurrenceFrequency, interval: Int, daysOfTheWeek days: [EKRecurrenceDayOfWeek]?, daysOfTheMonth monthDays: [NSNumber]?, monthsOfTheYear months: [NSNumber]?, weeksOfTheYear: [NSNumber]?, daysOfTheYear: [NSNumber]?, setPositions: [NSNumber]?, end: EKRecurrenceEnd?)
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)

#### Return Value

The initialized recurrence rule, or `nil` if invalid values are provided.

#### Discussion

Negative values indicate counting backwards from the end of the recurrence rule’s frequency.

## Parameters

- `type`: The frequency of the recurrence rule. Can be daily, weekly, monthly, or yearly.
- `interval`: The interval between instances of this recurrence. For example, a weekly recurrence rule with an interval of `2` occurs every other week. Must be greater than `0`.
- `days`: The days of the week that the event occurs, as an array of [`EKRecurrenceDayOfWeek`](ekrecurrencedayofweek.md) objects.
- `monthDays`: The days of the month that the event occurs, as an array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects. Values can be from `1` to `31` and from `-1` to `-31`. This parameter is only valid for recurrence rules of type [`EKRecurrenceFrequency.monthly`](ekrecurrencefrequency/monthly.md).
- `months`: The months of the year that the event occurs, as an array of `NSNumber` objects. Values can be from `1` to `12`. This parameter is only valid for recurrence rules of type [`EKRecurrenceFrequency.yearly`](ekrecurrencefrequency/yearly.md).
- `weeksOfTheYear`: The weeks of the year that the event occurs, as an array of `NSNumber` objects. Values can be from `1` to `53` and from `-1` to `-53`. This parameter is only valid for recurrence rules of type [`EKRecurrenceFrequency.yearly`](ekrecurrencefrequency/yearly.md).
- `daysOfTheYear`: The days of the year that the event occurs, as an array of `NSNumber` objects. Values can be from `1` to `366` and from `-1` to `-366`. This parameter is only valid for recurrence rules of type [`EKRecurrenceFrequency.yearly`](ekrecurrencefrequency/yearly.md).
- `setPositions`: An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency. See [`setPositions`](ekrecurrencerule/setpositions.md) for more information.
- `end`: The end of the recurrence rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/init(recurrencewith:interval:daysoftheweek:daysofthemonth:monthsoftheyear:weeksoftheyear:daysoftheyear:setpositions:end:))*