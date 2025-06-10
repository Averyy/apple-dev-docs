# NIDLTDOAMeasurement

**Framework**: Nearby Interaction  
**Kind**: class

Represents a single measurement relative to a DL-TDOA anchor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class NIDLTDOAMeasurement
```

## Topics

### Instance Properties
- [var address: Int](nidltdoameasurement/address.md)
  Indicates the address of anchor of this measurement.
- [var carrierFrequencyOffset: Double](nidltdoameasurement/carrierfrequencyoffset.md)
  Indicates the estimated carrier frequency offset (dimensionless).
- [var coordinates: simd_double3](nidltdoameasurement/coordinates.md)
  Indicates the anchor’s coordinates:
- [var coordinatesType: NIDLTDOACoordinatesType](nidltdoameasurement/coordinatestype.md)
  Inidicates the type of coordinates of this anchor.
- [var measurementType: NIDLTDOAMeasurementType](nidltdoameasurement/measurementtype.md)
  Indicates the type of this measurement.
- [var receiveTime: Double](nidltdoameasurement/receivetime.md)
  Indicates the reception timestamp (in seconds).
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  Indicates the signal strength in dBm.
- [var transmitTime: Double](nidltdoameasurement/transmittime.md)
  Indicates the transmission timestamp (in seconds).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement)*