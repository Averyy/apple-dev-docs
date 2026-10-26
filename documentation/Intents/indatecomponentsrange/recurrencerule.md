# recurrenceRule

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The rule for repeating the date range.

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
@NSCopying
var recurrenceRule: INRecurrenceRule? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INRecurrenceRule * recurrenceRule;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INRecurrenceRule * recurrenceRule;
```

## See Also

### Getting Recurring Date Information
- [func ekRecurrenceRule() -> EKRecurrenceRule?](./ekrecurrencerule%28%29.md)
  Returns an Event Kit recurrence rule that matches the available information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/recurrencerule)*