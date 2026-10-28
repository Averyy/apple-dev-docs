# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedTemperature: Measurement<UnitTemperature>) -> Self
```

```objc
+ (instancetype) successWithResolvedTemperature:(NSMeasurement<NSUnitTemperature *> *) resolvedTemperature;
```

## Return Value

A new [`INTemperatureResolutionResult`](../intemperatureresolutionresult.md) object.

## Discussion

Use this method to create a result object when you recognize the temperature value and are able to apply it to the vehicle settings.

## Parameters

- `resolvedTemperature`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: Measurement<UnitTemperature>?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [Measurement<UnitTemperature>]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemperatureresolutionresult/success(with:))*