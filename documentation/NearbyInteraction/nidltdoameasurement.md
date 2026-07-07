# NIDLTDOAMeasurement

**Framework**: Nearby Interaction  
**Kind**: class

Information from a Downlink Time-Difference-of-Arrival anchor that you use to derive a range estimate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class NIDLTDOAMeasurement
```

#### Overview

Your app runs on a receiver device that fields messages from nearby physical base stations, or *anchors*. The framework processes the messages into instances of this class and provides them to your app through the  [`session(_:didUpdateDLTDOA:)`](nisessiondelegate/session(_:didupdatedltdoa:).md) callback. Your app analyzes the measurements to calculate the receiver’s position relative to the anchors in the tracked area.

Only sessions that run a [`NIDLTDOAConfiguration`](nidltdoaconfiguration.md) receive Downlink Time-Difference-of-Arrival measurements.

## Topics

### Identifying the anchor
- [var address: Int](nidltdoameasurement/address.md)
  A value that uniquely identifies an anchor in a tracked area.
- [var clusterInitiatorAddress: Int](nidltdoameasurement/clusterinitiatoraddress.md)
  The address of the initiator anchor within the same cluster.
### Locating the anchor
- [var coordinates: simd_double3](nidltdoameasurement/coordinates.md)
  A triplet that represents the location in 3D space of the anchor that provides the measurement.
- [var coordinatesType: NIDLTDOACoordinatesType](nidltdoameasurement/coordinatestype.md)
  The type of coordinate system that the measurement conforms to.
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [var floorElevation: NIDLTDOAMeasurement.FloorElevation?](nidltdoameasurement/floorelevation-swift.property.md)
  The floor elevation information for the anchor, if available.
- [NIDLTDOAMeasurement.FloorElevation](nidltdoameasurement/floorelevation-swift.class.md)
  An object that describes how high off the ground DL-TDOA anchors reside in the environment.
### Assessing time difference
- [var receiveTime: Double](nidltdoameasurement/receivetime.md)
  A timestamp, in seconds, for the time that the device receives the measurement.
- [var transmitTime: Double](nidltdoameasurement/transmittime.md)
  A transmission timestamp, in seconds, for the received message.
### Evaluating the message
- [var measurementType: NIDLTDOAMeasurementType](nidltdoameasurement/measurementtype.md)
  The type of anchor message that the measurement derives from.
- [var carrierFrequencyOffset: Double](nidltdoameasurement/carrierfrequencyoffset.md)
  The drift, as a ratio, across the frequencies of the receiver and the anchor.
- [var responderClockFrequencyOffset: Double?](nidltdoameasurement/responderclockfrequencyoffset-8wu5r.md)
  The clock frequency offset of the responder anchor relative to the initiator anchor.
### Creating a measurement
- [init?(coder: NSCoder)](nidltdoameasurement/init(coder:).md)
### Instance Properties
- [var rawReceiveTime: UInt64](nidltdoameasurement/rawreceivetime.md)
  Indicates the raw reception timestamp (in units of 15.65 picoseconds).
- [var rawTransmitTime: UInt64](nidltdoameasurement/rawtransmittime.md)
  Indicates the raw transmission timestamp (in units of 15.65 picoseconds).

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

## See Also

- [enum NIDLTDOACoordinatesType](nidltdoacoordinatestype.md)
  The possible coordinate types for Downlink Time-Difference-of-Arrival measurement updates.
- [enum NIDLTDOAMeasurementType](nidltdoameasurementtype.md)
  The possible phases of downlink positioning signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement)*