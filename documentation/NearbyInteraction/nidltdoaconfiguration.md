# NIDLTDOAConfiguration

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

A configuration that enables Downlink Time-Difference-of-Arrival ranging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class NIDLTDOAConfiguration
```

```objc
@interface NIDLTDOAConfiguration : NIConfiguration
```

#### Overview

Run an instance of this configuration to participate in a session that supports the Downlink Time-Difference-of-Arrival (DL-TDOA) feature. Before creating an instance of this class, call [`supportsDLTDOAMeasurement`](./nidevicecapability/supportsdltdoameasurement.md) first to ensure device support.

## Topics

### Creating a configuration
- [init(networkIdentifier: Int)](./nidltdoaconfiguration/init%28networkidentifier%29.md)
  Initializes a Downlink Time-Difference-of-Arrival (DL-TDOA) configuration for a specific tracked area.
- [init(networkIdentifier: Int, discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod)](./nidltdoaconfiguration/init%28networkidentifier,discoverymethod%29.md)
  Initializes a DL-TDOA configuration with a network identifier and discovery method.
### Identifying the network
- [var networkIdentifier: Int](./nidltdoaconfiguration/networkidentifier.md)
  A unique identifier for a Downlink Time-Difference-of-Arrival network.
### Specifing the discovery method
- [var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod](./nidltdoaconfiguration/discoverymethod-swift.property.md)
  The technology your app uses to discover DL-TDOA anchors.
- [NIDLTDOAConfiguration.DiscoveryMethod](./nidltdoaconfiguration/discoverymethod-swift.enum.md)
  The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.

## Relationships

### Inherits From
- [NIConfiguration](./niconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration)*