# MediaOutputDevice.AuthorizationMethod

**Framework**: Media Device  
**Kind**: struct  
**Role**: Structure

Specifies what kind of authorization UI to present when connecting to a device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct AuthorizationMethod
```

## Mentions

- [Creating a media device extension](../creating-a-media-device-extension.md)

#### Overview

Use the provided factory methods to create an authorization method appropriate for your device’s pairing requirements.

## Topics

### Structures
- [MediaOutputDevice.AuthorizationMethod.CodeLength](./authorizationmethod/codelength.md)
  Represents the valid lengths for an authorization code.
### Type Properties
- [static var none: MediaOutputDevice.AuthorizationMethod](./authorizationmethod/none.md)
  No authorization is required.
- [static var password: MediaOutputDevice.AuthorizationMethod](./authorizationmethod/password.md)
  Presents a freeform text password input for device authorization.
### Type Methods
- [static func numericCode(length: MediaOutputDevice.AuthorizationMethod.CodeLength) -> MediaOutputDevice.AuthorizationMethod](./authorizationmethod/numericcode%28length%29.md)
  Creates a numeric PIN entry authorization method.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Device discovery and management
- [struct MediaOutputDevice](../mediaoutputdevice.md)
  Represents a discoverable media output device such as a TV, speaker, or streaming stick.
- [MediaOutputDevice.Capabilities](./capabilities-swift.struct.md)
  Defines the media capabilities supported by a [`MediaOutputDevice`](../mediaoutputdevice.md).
- [MediaOutputDevice.DeviceType](./devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](./volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/authorizationmethod)*