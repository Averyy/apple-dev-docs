# INTemporalEventTriggerTypeOptionsResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result that adds a temporal event trigger.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class INTemporalEventTriggerTypeOptionsResolutionResult
```

```objc
@interface INTemporalEventTriggerTypeOptionsResolutionResult : INIntentResolutionResult
```

#### Overview

You return an [`INTemporalEventTriggerTypeOptionsResolutionResult`](./intemporaleventtriggertypeoptionsresolutionresult.md) object when resolving parameters containing an [`INTemporalEventTriggerTypeOptions`](./intemporaleventtriggertypeoptions.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INTemporalEventTriggerTypeOptions) -> Self](./intemporaleventtriggertypeoptionsresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [class func confirmationRequired(with: INTemporalEventTriggerTypeOptions) -> Self](./intemporaleventtriggertypeoptionsresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Event Triggers
- [class INSpatialEventTrigger](./inspatialeventtrigger.md)
  A trigger condition based on the user’s arrival or departure from a given location.
- [class INTemporalEventTrigger](./intemporaleventtrigger.md)
  A trigger condition based on a date or time.
- [struct INDayOfWeekOptions](./indayofweekoptions.md)
  Days of the week.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggertypeoptionsresolutionresult)*