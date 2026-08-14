# MediaOutputDevice

**Framework**: Media Device  
**Kind**: struct

Represents a discoverable media output device such as a TV, speaker, or streaming stick.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct MediaOutputDevice
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

## Topics

### Structures
- [MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod.md)
  Specifies what kind of authorization UI to present when connecting to a device.
- [MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct.md)
  Defines the media capabilities supported by a [`MediaOutputDevice`](mediaoutputdevice.md).
### Operators
- [static func == (MediaOutputDevice, MediaOutputDevice) -> Bool](mediaoutputdevice/==(_:_:).md)
  Returns a Boolean value that indicates whether two devices are equal.
### Initializers
- [init?(id: UUID, displayName: String, capabilities: MediaOutputDevice.Capabilities, canGroupWithCurrentlyActivatedDevices: Bool, deviceType: MediaOutputDevice.DeviceType, volumeControl: MediaOutputDevice.VolumeControl, canMute: Bool, requiredNetworkEndpoints: [NWEndpoint], txtRecords: [NWTXTRecord], supportsSimultaneousSessions: Bool)](mediaoutputdevice/init(id:displayname:capabilities:cangroupwithcurrentlyactivateddevices:devicetype:volumecontrol:canmute:requirednetworkendpoints:txtrecords:supportssimultaneoussessions:).md)
  Creates a new media output device with the specified properties, requiring at least one network endpoint.
### Instance Properties
- [let canGroupWithCurrentlyActivatedDevices: Bool](mediaoutputdevice/cangroupwithcurrentlyactivateddevices.md)
  Indicates whether this device can be grouped with devices that are currently activated.
- [let canMute: Bool](mediaoutputdevice/canmute.md)
  Indicates whether the device supports muting audio output.
- [let capabilities: MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.property.md)
  The capabilities of the device.
- [var description: String](mediaoutputdevice/description.md)
  A textual representation of the device.
- [let deviceType: MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.property.md)
  The type of device, used for display in user interfaces.
- [let displayName: String](mediaoutputdevice/displayname.md)
  A display name for the device, shown in user interfaces.
- [let id: UUID](mediaoutputdevice/id.md)
  A unique identifier for the device.
- [let networkEndpoints: [NWEndpoint]](mediaoutputdevice/networkendpoints.md)
  The network endpoints for this device group.
- [let supportsSimultaneousSessions: Bool](mediaoutputdevice/supportssimultaneoussessions.md)
  Indicates whether the device supports receiving simultaneous media sessions via [`MediaOutputSession`](mediaoutputsession.md).
- [let txtRecords: [NWTXTRecord]](mediaoutputdevice/txtrecords.md)
  TXT records associated with the device discovered via network protocols.
- [let volumeControl: MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.property.md)
  The type of volume control supported by this device.
### Instance Methods
- [func hash(into: inout Hasher)](mediaoutputdevice/hash(into:).md)
  Hashes the essential components of the device by feeding them into the given hasher.
### Enumerations
- [MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct.md)
  Defines the media capabilities supported by a [`MediaOutputDevice`](mediaoutputdevice.md).
- [MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.
- [MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod.md)
  Specifies what kind of authorization UI to present when connecting to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice)*