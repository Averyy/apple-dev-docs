# MatterAddDeviceRequest

**Framework**: MatterSupport  
**Kind**: struct

A request that adds and sets up a device into an ecosystem.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct MatterAddDeviceRequest
```

## Topics

### Creating the request
- [init(from: any Decoder) throws](matteradddevicerequest/init(from:).md)
  Create the request from a decoder.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria)](matteradddevicerequest/init(topology:setuppayload:showing:).md)
  Create the request.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria, shouldScanNetworks: Bool)](matteradddevicerequest/init(topology:setuppayload:showing:shouldscannetworks:).md)
  Create the request with an optional network scan.
### Setting up the request
- [MatterAddDeviceRequest.Home](matteradddevicerequest/home.md)
  The representation of a home that appears in the picker during device setup.
- [MatterAddDeviceRequest.Room](matteradddevicerequest/room.md)
  The representation of a room that appears in the picker during device setup.
- [MatterAddDeviceRequest.Topology](matteradddevicerequest/topology-swift.struct.md)
  Information describing the properties of the ecosystem.
- [var setupPayload: MTRSetupPayload?](matteradddevicerequest/setuppayload.md)
  The payload to use for Matter device setup.
- [var topology: MatterAddDeviceRequest.Topology](matteradddevicerequest/topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.
### Defining the device criteria
- [MatterAddDeviceRequest.DeviceCriteria](matteradddevicerequest/devicecriteria.md)
  A predicate to match against possible devices that may appear in the picker.
- [var showDeviceCriteria: MatterAddDeviceRequest.DeviceCriteria](matteradddevicerequest/showdevicecriteria.md)
  A predicate that filters what devices appear in the picker.
### Performing the request
- [var shouldScanNetworks: Bool](matteradddevicerequest/shouldscannetworks.md)
  A flag that indicates whether to receive network scan results.
- [func perform() async throws](matteradddevicerequest/perform.md)
  Launch the user interface to set up a Matter device in the ecosystem.
### Type Properties
- [static var isSupported: Bool](matteradddevicerequest/issupported.md)
  A flag that indicates whether `MatterAddDeviceRequest` usage is supported
### Default Implementations
- [Decodable Implementations](matteradddevicerequest/decodable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding Matter support to your ecosystem](adding-matter-support-to-your-ecosystem.md)
  Allow people to add Matter accessories to your platform.
- [class MatterAddDeviceExtensionRequestHandler](matteradddeviceextensionrequesthandler.md)
  The object that handles configuration and commissioning of a device into an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest)*