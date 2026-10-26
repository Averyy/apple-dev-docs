# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedEnergy: Measurement<UnitEnergy>) -> Self
```

```objc
+ (instancetype) successWithResolvedEnergy:(NSMeasurement<NSUnitEnergy *> *) resolvedEnergy;
```

#### Return Value

A new [`INEnergyResolutionResult`](../inenergyresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you can resolve a parameter successfully to a value in your own internal data structures.

## Parameters

- `resolvedEnergy`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: Measurement<UnitEnergy>?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [Measurement<UnitEnergy>]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inenergyresolutionresult/success(with:))*