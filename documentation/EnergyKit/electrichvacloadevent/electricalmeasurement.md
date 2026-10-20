# ElectricHVACLoadEvent.ElectricalMeasurement

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A description of the electricity consumed by a device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct ElectricalMeasurement
```

## Topics

### Initializing an electrical measurement
- [init(stage: Int)](./electricalmeasurement/init%28stage%29.md)
  Initializes an electrical measurement for the electrical load event.
- [let stage: Int](./electricalmeasurement/stage.md)
  An indirect measurement of power consumption by an HVAC electric heating or cooling stage.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting electrical measurements
- [let measurement: ElectricHVACLoadEvent.ElectricalMeasurement](./measurement.md)
  The electricity consumption of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/electricalmeasurement)*