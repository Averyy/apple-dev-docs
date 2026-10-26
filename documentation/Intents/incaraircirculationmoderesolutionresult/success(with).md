# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class func success(with resolvedCarAirCirculationMode: INCarAirCirculationMode) -> Self
```

```objc
+ (instancetype) successWithResolvedCarAirCirculationMode:(INCarAirCirculationMode) resolvedCarAirCirculationMode;
```

#### Return Value

A new [`INCarAirCirculationModeResolutionResult`](../incaraircirculationmoderesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you recognize the air circulation mode and are able to modify it.

## Parameters

- `resolvedCarAirCirculationMode`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCarAirCirculationMode) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incaraircirculationmoderesolutionresult/success(with:))*