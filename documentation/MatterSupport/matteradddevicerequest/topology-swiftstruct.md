# MatterAddDeviceRequest.Topology

**Framework**: MatterSupport  
**Kind**: struct

Information describing the properties of the ecosystem.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct Topology
```

#### Overview

The topology of a fabric consists of its homes, rooms, and devices. The number of homes included in this class determines whether the setup presents a home selection step. If there are two or more homes, the user selects one home to add the device to.

## Topics

### Creating the topology
- [init(from: any Decoder) throws](matteradddevicerequest/init(from:).md)
  Create the request from a decoder.
- [init(ecosystemName: String, homes: [MatterAddDeviceRequest.Home])](matteradddevicerequest/topology-swift.struct/init(ecosystemname:homes:).md)
  Creates the topology.
### Getting the properties
- [var ecosystemName: String](matteradddevicerequest/topology-swift.struct/ecosystemname.md)
  The name of your ecosystem.
- [var homes: [MatterAddDeviceRequest.Home]](matteradddevicerequest/topology-swift.struct/homes.md)
  An array of available homes to add the new device into.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MatterAddDeviceRequest.Home](matteradddevicerequest/home.md)
  The representation of a home that appears in the picker during device setup.
- [MatterAddDeviceRequest.Room](matteradddevicerequest/room.md)
  The representation of a room that appears in the picker during device setup.
- [var setupPayload: MTRSetupPayload?](matteradddevicerequest/setuppayload.md)
  The payload to use for Matter device setup.
- [var topology: MatterAddDeviceRequest.Topology](matteradddevicerequest/topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/topology-swift.struct)*