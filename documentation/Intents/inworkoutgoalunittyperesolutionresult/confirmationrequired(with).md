# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the workout unit goal value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with workoutGoalUnitTypeToConfirm: INWorkoutGoalUnitType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithWorkoutGoalUnitTypeToConfirm:(INWorkoutGoalUnitType) workoutGoalUnitTypeToConfirm;
```

#### Return Value

A new [`INWorkoutGoalUnitTypeResolutionResult`](../inworkoutgoalunittyperesolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to a similar workout goal and want the user to confirm the change before proceeding.

## Parameters

- `workoutGoalUnitTypeToConfirm`: The object that resolves the request. The information in this object must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INWorkoutGoalUnitType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutgoalunittyperesolutionresult/confirmationrequired(with:))*