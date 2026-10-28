# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedWorkoutGoalUnitType: INWorkoutGoalUnitType) -> Self
```

```objc
+ (instancetype) successWithResolvedWorkoutGoalUnitType:(INWorkoutGoalUnitType) resolvedWorkoutGoalUnitType;
```

## Return Value

A new [`INWorkoutGoalUnitTypeResolutionResult`](../inworkoutgoalunittyperesolutionresult.md) object.

## Discussion

Use this method to create a result object when you recognize the goal type and can use it to track the user’s progress.

## Parameters

- `resolvedWorkoutGoalUnitType`: The value that resolves the intent’s requested parameter. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INWorkoutGoalUnitType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the workout unit goal value before proceeding.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutgoalunittyperesolutionresult/success(with:))*