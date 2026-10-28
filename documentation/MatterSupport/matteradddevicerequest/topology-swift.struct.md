# MatterAddDeviceRequest.Topology

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

Information describing the properties of the ecosystem.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct Topology
```

## Overview

The topology of a fabric consists of its homes, rooms, and devices. The number of homes included in this class determines whether the setup presents a home selection step. If there are two or more homes, the user selects one home to add the device to.

## Topics

### Creating the topology
- [init(from: any Decoder) throws](./init%28from%29.md)
  Create the request from a decoder.
- [init(ecosystemName: String, homes: [MatterAddDeviceRequest.Home])](./topology-swift.struct/init%28ecosystemname,homes%29.md)
  Creates the topology.
### Getting the properties
- [var ecosystemName: String](./topology-swift.struct/ecosystemname.md)
  The name of your ecosystem.
- [var homes: [MatterAddDeviceRequest.Home]](./topology-swift.struct/homes.md)
  An array of available homes to add the new device into.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting up the request
- [MatterAddDeviceRequest.Home](./home.md)
  The representation of a home that appears in the picker during device setup.
- [MatterAddDeviceRequest.Room](./room.md)
  The representation of a room that appears in the picker during device setup.
- [var setupPayload: MTRSetupPayload?](./setuppayload.md)
  The payload to use for Matter device setup.
- [var topology: MatterAddDeviceRequest.Topology](./topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/topology-swift.struct)*