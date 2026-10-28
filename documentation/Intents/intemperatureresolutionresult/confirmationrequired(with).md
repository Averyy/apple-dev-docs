# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with temperatureToConfirm: Measurement<UnitTemperature>?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTemperatureToConfirm:(NSMeasurement<NSUnitTemperature *> *) temperatureToConfirm;
```

## Return Value

A new [`INTemperatureResolutionResult`](../intemperatureresolutionresult.md) object.

## Discussion

Use this method when you can resolve the parameter to an equivalent value and want the user to confirm the replacement value before proceeding.

## Parameters

- `temperatureToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: Measurement<UnitTemperature>) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [Measurement<UnitTemperature>]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemperatureresolutionresult/confirmationrequired(with:))*