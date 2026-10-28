# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with workoutLocationTypeToConfirm: INWorkoutLocationType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithWorkoutLocationTypeToConfirm:(INWorkoutLocationType) workoutLocationTypeToConfirm;
```

## Return Value

A new [`INWorkoutLocationTypeResolutionResult`](../inworkoutlocationtyperesolutionresult.md) object.

## Discussion

Use this method when you can resolve the parameter to a similar workout location and want the user to confirm that location choice.

## Parameters

- `workoutLocationTypeToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INWorkoutLocationType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutlocationtyperesolutionresult/confirmationrequired(with:))*