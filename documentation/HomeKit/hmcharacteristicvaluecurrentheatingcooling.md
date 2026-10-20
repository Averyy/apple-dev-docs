# HMCharacteristicValueCurrentHeatingCooling

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

States that indicate an accessory’s process of increasing or decreasing temperature.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HMCharacteristicValueCurrentHeatingCooling
```

```c
enum HMCharacteristicValueCurrentHeatingCooling : NSInteger;
```

## Topics

### Temperature States
- [HMCharacteristicValueCurrentHeatingCooling.cool](./hmcharacteristicvaluecurrentheatingcooling/cool.md)
  The accessory state indicates cooling.
- [HMCharacteristicValueCurrentHeatingCooling.heat](./hmcharacteristicvaluecurrentheatingcooling/heat.md)
  The accessory state indicates heating.
- [HMCharacteristicValueCurrentHeatingCooling.off](./hmcharacteristicvaluecurrentheatingcooling/off.md)
  The accessory indicates no heating or cooling.
### Initializers
- [init?(rawValue: Int)](./hmcharacteristicvaluecurrentheatingcooling/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Values
- [enum HMCharacteristicValueHeatingCooling](./hmcharacteristicvalueheatingcooling.md)
  Possible values for the heating or cooling characteristic of a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentheatingcooling)*