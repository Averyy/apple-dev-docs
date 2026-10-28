# ElectricalLoadEventProtocol

**Framework**: EnergyKit  
**Kind**: protocol  
**Role**: Protocol

A type that can represent an electrical load event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
protocol ElectricalLoadEventProtocol : Decodable, Encodable, Identifiable, Sendable
```

## Mentions

- [Providing charging history for electric vehicles](./providing-informative-charging-history-for-electric-vehicles.md)

## Overview

Don’t declare new conformances to `ElectricalLoadEventProtocol`. Only [`ElectricVehicleLoadEvent`](./electricvehicleloadevent.md) and [`ElectricHVACLoadEvent`](./electrichvacloadevent.md) can conform to `ElectricalLoadEventProtocol`.

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [ElectricHVACLoadEvent](./electrichvacloadevent.md)
- [ElectricVehicleLoadEvent](./electricvehicleloadevent.md)
- [ElectricVehicleStatusEvent](./electricvehiclestatusevent.md)

## See Also

### Device identification
- [struct ElectricalLoadDevice](./electricalloaddevice.md)
  A type that identifies an electrical load device for event submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricalloadeventprotocol)*