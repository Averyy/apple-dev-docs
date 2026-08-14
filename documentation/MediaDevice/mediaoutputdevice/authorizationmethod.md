# MediaOutputDevice.AuthorizationMethod

**Framework**: Media Device  
**Kind**: struct

Specifies what kind of authorization UI to present when connecting to a device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AuthorizationMethod
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Overview

Use the provided factory methods to create an authorization method appropriate for your device’s pairing requirements.

## Topics

### Structures
- [MediaOutputDevice.AuthorizationMethod.CodeLength](mediaoutputdevice/authorizationmethod/codelength.md)
  Represents the valid lengths for an authorization code.
### Type Properties
- [static var none: MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod/none.md)
  No authorization is required.
- [static var password: MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod/password.md)
  Presents a freeform text password input for device authorization.
### Type Methods
- [static func numericCode(length: MediaOutputDevice.AuthorizationMethod.CodeLength) -> MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod/numericcode(length:).md)
  Creates a numeric PIN entry authorization method.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct MediaOutputDevice](mediaoutputdevice.md)
  Represents a discoverable media output device such as a TV, speaker, or streaming stick.
- [MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct.md)
  Defines the media capabilities supported by a [`MediaOutputDevice`](mediaoutputdevice.md).
- [MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/authorizationmethod)*