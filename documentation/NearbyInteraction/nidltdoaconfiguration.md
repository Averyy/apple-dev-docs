# NIDLTDOAConfiguration

**Framework**: Nearby Interaction  
**Kind**: class

A configuration that enables Downlink Time-Difference-of-Arrival ranging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class NIDLTDOAConfiguration
```

#### Overview

Run an instance of this configuration to participate in a session that supports the Downlink Time-Difference-of-Arrival (DL-TDoA) feature. Before creating an instance of this class, call [`supportsDLTDOAMeasurement`](nidevicecapability/supportsdltdoameasurement.md) first to ensure device support.

DL-TDoA is an Ultra Wideband (UWB) ranging strategy that can produce sub-meter (0.5 - 1 meter) location support for tracked devices in a well-defined area. The solution works by installing base stations, or , within the tracked area. The anchors send messages to receiver devices that support DL-TDoA, such as iPhone 12 and later, and the receivers use the messages to calculate their location.

##### Receive Measurements and Calculate the Devices Location

When a device receives a message from an anchor, the framework creates the measurement object [`NIDLTDOAMeasurement`](nidltdoameasurement.md) and provides it to your app by invoking the  [`session(_:didUpdateDLTDOA:)`](nisessiondelegate/session(_:didupdatedltdoa:).md) callback. The measurement contains the coordinates of the anchor in the physical environment and the time it takes the message to arrive. Your app uses the anchor’s coordinates and the elapsed message-transmission time to calculate the device’s location. The calculation consists of a comparison of measurements from multiple anchors, and in particular, the difference in their arrival time to the receiver.

##### Distinguish and Determine the Tracked Area

Provide a network identifier when instantiating this class to distinguish among different tracked areas when there are multiple tracked areas in the vicinity. The network identifier is the session ID in the anchor’s DL-TDoA configuration. Your app can infer the range of an anchor by changes in its signal strength. The anchor’s range, coordinates, and network ID together compose the bounds of the tracked area.

## Topics

### Creating a configuration
- [init(networkIdentifier: Int)](nidltdoaconfiguration/init(networkidentifier:).md)
  Initializes a Downlink Time-Difference-of-Arrival (DL-TDoA) configuration for a specific tracked area.
### Identifying the network
- [var networkIdentifier: Int](nidltdoaconfiguration/networkidentifier.md)
  A unique identifier for a Downlink Time-Difference-of-Arrival network.

## Relationships

### Inherits From
- [NIConfiguration](niconfiguration.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration)*