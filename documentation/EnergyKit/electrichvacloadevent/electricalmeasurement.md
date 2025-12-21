# ElectricHVACLoadEvent.ElectricalMeasurement

**Framework**: EnergyKit  
**Kind**: struct

A description of the electricity consumed by a device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct ElectricalMeasurement
```

## Topics

### Initializing an electrical measurement
- [init(stage: Int)](electrichvacloadevent/electricalmeasurement/init(stage:).md)
  Initializes an electrical measurement for the electrical load event.
- [let stage: Int](electrichvacloadevent/electricalmeasurement/stage.md)
  An indirect measurement of power consumption by an HVAC electric heating or cooling stage.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, deviceID: String)](electrichvacloadevent/init(timestamp:measurement:session:deviceid:).md)
  Creates an electric HVAC load event.
- [ElectricHVACLoadEvent.Session](electrichvacloadevent/session-swift.struct.md)
  A session that tracks the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/electricalmeasurement)*