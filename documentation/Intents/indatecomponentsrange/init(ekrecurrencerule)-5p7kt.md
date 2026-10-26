# init(ekRecurrenceRule:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the date range using the specified recurrence rule.

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
convenience init(ekRecurrenceRule recurrenceRule: EKRecurrenceRule)
```

```objc
- (instancetype) initWithEKRecurrenceRule:(EKRecurrenceRule *) recurrenceRule;
```

#### Return Value

An initialized [`INDateComponentsRange`](../indatecomponentsrange.md) object.

#### Discussion

Use this method to initialize the date range from Event Kit recurrence rules. For example, apps that support the creation of calendar events and reminders using Event Kit might use this method to specify date ranges when processing intents.

## Parameters

- `recurrenceRule`: An Event Kit recurrence rule.

## See Also

### Initializing a Date Components Range
- [convenience init(start: DateComponents?, end: DateComponents?)](./init%28start,end%29.md)
  Initializes the object using the specified start and end dates.
- [init(start: DateComponents?, end: DateComponents?, recurrenceRule: INRecurrenceRule?)](./init%28start,end,recurrencerule%29.md)
  Initializes the date range to a repeating time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/init(ekrecurrencerule:)-5p7kt)*