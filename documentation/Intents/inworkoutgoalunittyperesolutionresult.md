# INWorkoutGoalUnitTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the units of a workout goal.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INWorkoutGoalUnitTypeResolutionResult
```

```objc
@interface INWorkoutGoalUnitTypeResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INWorkoutGoalUnitTypeResolutionResult`](./inworkoutgoalunittyperesolutionresult.md) object is what you return when resolving parameters that contain a [`INWorkoutGoalUnitType`](./inworkoutgoalunittype.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INWorkoutGoalUnitType) -> Self](./inworkoutgoalunittyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [class func confirmationRequired(with: INWorkoutGoalUnitType) -> Self](./inworkoutgoalunittyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the workout unit goal value before proceeding.

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

### Resolution Results
- [class INWorkoutLocationTypeResolutionResult](./inworkoutlocationtyperesolutionresult.md)
  A resolution result for the location type where the workout occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutgoalunittyperesolutionresult)*