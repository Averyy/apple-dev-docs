# init(start:end:recurrenceRule:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the date range to a repeating time period.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(start startDateComponents: DateComponents?, end endDateComponents: DateComponents?, recurrenceRule: INRecurrenceRule?)
```

```objc
- (instancetype) initWithStartDateComponents:(NSDateComponents *) startDateComponents endDateComponents:(NSDateComponents *) endDateComponents recurrenceRule:(INRecurrenceRule *) recurrenceRule;
```

## Return Value

An initialized [`INDateComponentsRange`](../indatecomponentsrange.md) object.

## Discussion

Use this method to initialize a date range that repeats over time. For example, you could create a range that represents the time range of “every wednesday”. Use the start and end dates to specify the date and time values that you want to repeat and use the `recurrenceRule` property to establish the conditions for repeating the value.

## Parameters

- `startDateComponents`: The starting date for the time range. This value is assigned to the [`startDateComponents`](./startdatecomponents.md) property. Specify `nil` if you want the time range to start in the distant past.
- `endDateComponents`: The starting date for the time range. This value is assigned to the [`endDateComponents`](./enddatecomponents.md) property. Specify `nil` if you want the time range to end in the distant future.
- `recurrenceRule`: The recurrence rule to use when repeating the date range.

## See Also

### Initializing a Date Components Range
- [convenience init(start: DateComponents?, end: DateComponents?)](./init%28start,end%29.md)
  Initializes the object using the specified start and end dates.
- [convenience init(ekRecurrenceRule: EKRecurrenceRule)](./init%28ekrecurrencerule%29-5p7kt.md)
  Initializes the date range using the specified recurrence rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/init(start:end:recurrencerule:))*