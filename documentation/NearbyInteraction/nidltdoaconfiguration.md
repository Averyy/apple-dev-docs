# NIDLTDOAConfiguration

**Framework**: Nearby Interaction  
**Kind**: class

A configuration that enables Downlink Time-Difference-of-Arrival ranging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class NIDLTDOAConfiguration
```

#### Overview

Run an instance of this configuration to participate in a session that supports the Downlink Time-Difference-of-Arrival (DL-TDOA) feature. Before creating an instance of this class, call [`supportsDLTDOAMeasurement`](nidevicecapability/supportsdltdoameasurement.md) first to ensure device support.

## Topics

### Creating a configuration
- [init(networkIdentifier: Int)](nidltdoaconfiguration/init(networkidentifier:).md)
  Initializes a Downlink Time-Difference-of-Arrival (DL-TDOA) configuration for a specific tracked area.
- [init(networkIdentifier: Int, discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod)](nidltdoaconfiguration/init(networkidentifier:discoverymethod:).md)
  Initializes a DL-TDOA configuration with a network identifier and discovery method.
### Identifying the network
- [var networkIdentifier: Int](nidltdoaconfiguration/networkidentifier.md)
  A unique identifier for a Downlink Time-Difference-of-Arrival network.
### Specifing the discovery method
- [var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod](nidltdoaconfiguration/discoverymethod-swift.property.md)
  The technology your app uses to discover DL-TDOA anchors.
- [NIDLTDOAConfiguration.DiscoveryMethod](nidltdoaconfiguration/discoverymethod-swift.enum.md)
  The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.

## Relationships

### Inherits From
- [NIConfiguration](niconfiguration.md)
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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration)*