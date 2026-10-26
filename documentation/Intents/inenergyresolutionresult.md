# INEnergyResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for an energy parameter associated with an intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INEnergyResolutionResult
```

```objc
@interface INEnergyResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INEnergyResolutionResult`](./inenergyresolutionresult.md) object is what you return when resolving energy related parameters of an intent object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: Measurement<UnitEnergy>) -> Self](./inenergyresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: Measurement<UnitEnergy>?) -> Self](./inenergyresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [Measurement<UnitEnergy>]) -> Self](./inenergyresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

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

### Measurements
- [class INLengthResolutionResult](./inlengthresolutionresult.md)
  A resolution result for a length associated with an intent.
- [class INMassResolutionResult](./inmassresolutionresult.md)
  A resolution result for a mass associated with an intent.
- [class INSpeedResolutionResult](./inspeedresolutionresult.md)
  A resolution result for a speed associated with an intent.
- [class INTemperatureResolutionResult](./intemperatureresolutionresult.md)
  A resolution result for the units to use with a temperature value.
- [class INVolumeResolutionResult](./involumeresolutionresult.md)
  A resolution result for a volume associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inenergyresolutionresult)*