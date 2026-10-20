# MatterAddDeviceRequest.Home

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

The representation of a home that appears in the picker during device setup.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct Home
```

## Topics

### Creating the home
- [init(from: any Decoder) throws](./init%28from%29.md)
  Create the request from a decoder.
- [init(displayName: String)](./home/init%28displayname%29.md)
  Creates a new home.
### Getting the properties
- [var displayName: String](./home/displayname.md)
  The name of the home that appears in the picker.

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
- [MatterAddDeviceRequest.Room](./room.md)
  The representation of a room that appears in the picker during device setup.
- [MatterAddDeviceRequest.Topology](./topology-swift.struct.md)
  Information describing the properties of the ecosystem.
- [var setupPayload: MTRSetupPayload?](./setuppayload.md)
  The payload to use for Matter device setup.
- [var topology: MatterAddDeviceRequest.Topology](./topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/home)*