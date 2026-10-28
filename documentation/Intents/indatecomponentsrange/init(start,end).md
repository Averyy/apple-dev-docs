# init(start:end:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object using the specified start and end dates.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(start startDateComponents: DateComponents?, end endDateComponents: DateComponents?)
```

```objc
- (instancetype) initWithStartDateComponents:(NSDateComponents *) startDateComponents endDateComponents:(NSDateComponents *) endDateComponents;
```

## Return Value

An initialized [`INDateComponentsRange`](../indatecomponentsrange.md) object.

## Discussion

Use this method to initialize a date range with specific parameters. In a date components object, include only the values you want to specify, such as a range that measures only in days or a range that measures only in minutes.

## Parameters

- `startDateComponents`: The starting date for the time range assigned to the [`startDateComponents`](./startdatecomponents.md) property. Specify `nil` if you want the time range to start in the distant past.
- `endDateComponents`: The ending date for the time range assigned to the [`endDateComponents`](./enddatecomponents.md) property. Specify `nil` if you want the time range to end in the distant future.

## See Also

### Initializing a Date Components Range
- [init(start: DateComponents?, end: DateComponents?, recurrenceRule: INRecurrenceRule?)](./init%28start,end,recurrencerule%29.md)
  Initializes the date range to a repeating time period.
- [convenience init(ekRecurrenceRule: EKRecurrenceRule)](./init%28ekrecurrencerule%29-5p7kt.md)
  Initializes the date range using the specified recurrence rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/init(start:end:))*