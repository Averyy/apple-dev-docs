# ekRecurrenceRule()

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Returns an Event Kit recurrence rule that matches the available information.

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
func ekRecurrenceRule() -> EKRecurrenceRule?
```

```objc
- (EKRecurrenceRule *) EKRecurrenceRule;
```

## Return Value

The recurrence rule that matches the recurring date range, or nil if the date components range does not specify a recurring time.

## Discussion

If you initialized the date components range with a recurrence rule, use this method to specify that rule in a format that is accepted by Event Kit classes.

## See Also

### Getting Recurring Date Information
- [var recurrenceRule: INRecurrenceRule?](./recurrencerule.md)
  The rule for repeating the date range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/ekrecurrencerule())*