# INDayOfWeekOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Days of the week.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct INDayOfWeekOptions
```

```c
enum INDayOfWeekOptions : NSUInteger;
```

## Topics

### Days of the Week
- [static var monday: INDayOfWeekOptions](./indayofweekoptions/monday.md)
  The value for Monday.
- [static var tuesday: INDayOfWeekOptions](./indayofweekoptions/tuesday.md)
  The value for Tuesday.
- [static var wednesday: INDayOfWeekOptions](./indayofweekoptions/wednesday.md)
  The value for Wednesday.
- [static var thursday: INDayOfWeekOptions](./indayofweekoptions/thursday.md)
  The value for Thursday.
- [static var friday: INDayOfWeekOptions](./indayofweekoptions/friday.md)
  The value for Friday.
- [static var saturday: INDayOfWeekOptions](./indayofweekoptions/saturday.md)
  The value for Saturday.
- [static var sunday: INDayOfWeekOptions](./indayofweekoptions/sunday.md)
  The value for Sunday.
### Initializing a Set of Days
- [init(rawValue: UInt)](./indayofweekoptions/init%28rawvalue%29.md)
  Initializes a set that contains the specified days of the week.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Event Triggers
- [class INSpatialEventTrigger](./inspatialeventtrigger.md)
  A trigger condition based on the user’s arrival or departure from a given location.
- [class INTemporalEventTrigger](./intemporaleventtrigger.md)
  A trigger condition based on a date or time.
- [class INTemporalEventTriggerTypeOptionsResolutionResult](./intemporaleventtriggertypeoptionsresolutionresult.md)
  A resolution result that adds a temporal event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indayofweekoptions)*