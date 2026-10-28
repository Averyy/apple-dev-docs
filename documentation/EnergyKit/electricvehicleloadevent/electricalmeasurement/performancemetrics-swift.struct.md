# ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

Performance metrics for the current electrical measurement.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
struct PerformanceMetrics
```

## Overview

Performance metrics provide additional context about the vehicle’s state during charging, such as the estimated driving range and battery temperature.

## Topics

### Creating performance metrics
- [init(estimatedRange: Measurement<UnitLength>?, batteryTemperature: Measurement<UnitTemperature>?)](./performancemetrics-swift.struct/init%28estimatedrange,batterytemperature%29.md)
  Creates performance metrics for the current measurement.
### Getting performance data
- [let estimatedRange: Measurement<UnitLength>?](./performancemetrics-swift.struct/estimatedrange.md)
  An estimate of how far the vehicle can travel based on the current state of charge.
- [let batteryTemperature: Measurement<UnitTemperature>?](./performancemetrics-swift.struct/batterytemperature.md)
  A battery pack temperature.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting performance metrics
- [var performanceMetrics: ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics?](./performancemetrics-swift.property.md)
  Performance metrics for an electrical measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct)*