# CMWaterTemperature

**Framework**: Core Motion  
**Kind**: class

An update that contains data about the water temperature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CMWaterTemperature
```

## Topics

### Accessing the data
- [var date: Date](cmwatertemperature/date.md)
  The time and date when the system recorded the measurements.
- [var temperature: Measurement<UnitTemperature>](cmwatertemperature/temperature.md)
  The water temperature.
- [var temperatureUncertainty: Measurement<UnitTemperature>](cmwatertemperature/temperatureuncertainty.md)
  The amount of uncertainty in the measurement of the water temperature.
### Initializers
- [init?(coder: NSCoder)](cmwatertemperature/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Accessing submersion data](accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [class CMWaterSubmersionManager](cmwatersubmersionmanager.md)
  An object for managing the collection of pressure and temperature data during submersion.
- [protocol CMWaterSubmersionManagerDelegate](cmwatersubmersionmanagerdelegate.md)
  A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- [class CMWaterSubmersionEvent](cmwatersubmersionevent.md)
  An event indicating that the device’s submersion state has changed.
- [class CMWaterSubmersionMeasurement](cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatertemperature)*