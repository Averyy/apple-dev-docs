# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedWorkoutLocationType: INWorkoutLocationType) -> Self
```

```objc
+ (instancetype) successWithResolvedWorkoutLocationType:(INWorkoutLocationType) resolvedWorkoutLocationType;
```

#### Return Value

A new [`INWorkoutLocationTypeResolutionResult`](../inworkoutlocationtyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you recognize the specified workout location.

## Parameters

- `resolvedWorkoutLocationType`: The object that resolves the intent’s requested parameter. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INWorkoutLocationType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutlocationtyperesolutionresult/success(with:))*