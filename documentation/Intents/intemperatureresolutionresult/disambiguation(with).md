# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func disambiguation(with temperaturesToDisambiguate: [Measurement<UnitTemperature>]) -> Self
```

```objc
+ (instancetype) disambiguationWithTemperaturesToDisambiguate:(NSArray<NSMeasurement<NSUnitTemperature *> *> *) temperaturesToDisambiguate;
```

## Return Value

A new [`INTemperatureResolutionResult`](../intemperatureresolutionresult.md) object.

## Discussion

Use this method to create a result object when there is more one value that might match the given parameter. Siri asks the user to select from among the measurement values that you specify.

## Parameters

- `temperaturesToDisambiguate`: An array of [`NSMeasurement`](../../Foundation/nsmeasurement.md) objects for the user to choose from. Each measurement object reflects a value of type [`UnitTemperature`](../../Foundation/unittemperature.md).

## See Also

### Creating a Resolution Result Object
- [class func success(with: Measurement<UnitTemperature>) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: Measurement<UnitTemperature>?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemperatureresolutionresult/disambiguation(with:))*