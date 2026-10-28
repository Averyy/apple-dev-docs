# INWorkoutLocationTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the location type where the workout occurs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INWorkoutLocationTypeResolutionResult
```

```objc
@interface INWorkoutLocationTypeResolutionResult : INIntentResolutionResult
```

## Overview

You return an [`INWorkoutLocationTypeResolutionResult`](./inworkoutlocationtyperesolutionresult.md) object when resolving parameters containing a [`INWorkoutLocationType`](./inworkoutlocationtype.md) value. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INWorkoutLocationType) -> Self](./inworkoutlocationtyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INWorkoutLocationType) -> Self](./inworkoutlocationtyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./inworkoutlocationtyperesolutionresult/successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./inworkoutlocationtyperesolutionresult/confirmationrequiredwithvaluetoconfirm_.md)

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
- [class INWorkoutGoalUnitTypeResolutionResult](./inworkoutgoalunittyperesolutionresult.md)
  A resolution result for the units of a workout goal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutlocationtyperesolutionresult)*