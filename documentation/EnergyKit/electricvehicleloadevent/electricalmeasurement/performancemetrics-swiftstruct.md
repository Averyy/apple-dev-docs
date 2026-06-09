# ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics

**Framework**: EnergyKit  
**Kind**: struct

Performance metrics for the current electrical measurement.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct PerformanceMetrics
```

#### Overview

Performance metrics provide additional context about the vehicle’s state during charging, such as the estimated driving range and battery temperature.

## Topics

### Creating performance metrics
- [init(estimatedRange: Measurement<UnitLength>?, batteryTemperature: Measurement<UnitTemperature>?)](electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct/init(estimatedrange:batterytemperature:).md)
  Creates performance metrics for the current measurement.
### Getting performance data
- [let estimatedRange: Measurement<UnitLength>?](electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct/estimatedrange.md)
  An estimate of how far the vehicle can travel based on the current state of charge.
- [let batteryTemperature: Measurement<UnitTemperature>?](electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct/batterytemperature.md)
  A battery pack temperature.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var performanceMetrics: ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics?](electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.property.md)
  Performance metrics for an electrical measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct)*