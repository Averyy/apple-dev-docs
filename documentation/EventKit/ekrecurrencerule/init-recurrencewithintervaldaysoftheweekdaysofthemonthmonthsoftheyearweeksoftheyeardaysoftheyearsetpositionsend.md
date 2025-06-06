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
- `interval`: The interval between instances of this recurrence. For example, a weekly recurrence rule with an interval of   occurs every other week. Must be greater than  .
- `days`: The days of the week that the event occurs, as an array of   objects.
- `monthDays`: The days of the month that the event occurs, as an array of   objects. Values can be from   to   and from   to  . This parameter is only valid for recurrence rules of type  .
- `months`: The months of the year that the event occurs, as an array of   objects. Values can be from   to  . This parameter is only valid for recurrence rules of type  .
- `weeksOfTheYear`: The weeks of the year that the event occurs, as an array of   objects. Values can be from   to   and from   to  . This parameter is only valid for recurrence rules of type  .
- `daysOfTheYear`: The days of the year that the event occurs, as an array of   objects. Values can be from   to   and from   to  . This parameter is only valid for recurrence rules of type  .
- `setPositions`: An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency. See   for more information.
- `end`: The end of the recurrence rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/init(recurrencewith:interval:daysoftheweek:daysofthemonth:monthsoftheyear:weeksoftheyear:daysoftheyear:setpositions:end:))*