# MatterAddDeviceRequest.Room

**Framework**: MatterSupport  
**Kind**: struct

The representation of a room that appears in the picker during device setup.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct Room
```

## Topics

### Creating the room
- [init(from: any Decoder) throws](matteradddevicerequest/init(from:).md)
  Create the request from a decoder.
- [init(displayName: String)](matteradddevicerequest/room/init(displayname:).md)
  Creates a new room.
### Getting the properties
- [var displayName: String](matteradddevicerequest/room/displayname.md)
  The name of the room that appears in the picker.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MatterAddDeviceRequest.Home](matteradddevicerequest/home.md)
  The representation of a home that appears in the picker during device setup.
- [MatterAddDeviceRequest.Topology](matteradddevicerequest/topology-swift.struct.md)
  Information describing the properties of the ecosystem.
- [var setupPayload: MTRSetupPayload?](matteradddevicerequest/setuppayload.md)
  The payload to use for Matter device setup.
- [var topology: MatterAddDeviceRequest.Topology](matteradddevicerequest/topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/room)*