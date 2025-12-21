# NIDLTDOAMeasurementType

**Framework**: Nearby Interaction  
**Kind**: enum

The possible phases of downlink positioning signals.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum NIDLTDOAMeasurementType
```

#### Overview

The [`NIDLTDOAMeasurement`](nidltdoameasurement.md) class [`measurementType`](nidltdoameasurement/measurementtype.md) property is of this type.

## Topics

### Identifying the measurement type
- [NIDLTDOAMeasurementType.poll](nidltdoameasurementtype/poll.md)
  A type that indicates the measurement derives from an initiating anchor’s first message.
- [NIDLTDOAMeasurementType.response](nidltdoameasurementtype/response.md)
  A type that indicates the measurement derives from responder anchors’ messages.
- [NIDLTDOAMeasurementType.final](nidltdoameasurementtype/final.md)
  A type that indicates the measurement derives from an initial anchor’s last message.
### Creating a measurement type
- [init?(rawValue: Int)](nidltdoameasurementtype/init(rawvalue:).md)
  Creates a measurement type from the given underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NIDLTDOAMeasurement](nidltdoameasurement.md)
  Information from a Downlink Time-Difference-of-Arrival anchor that you use to derive a range estimate.
- [enum NIDLTDOACoordinatesType](nidltdoacoordinatestype.md)
  The possible coordinate types for Downlink Time-Difference-of-Arrival measurement updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurementtype)*