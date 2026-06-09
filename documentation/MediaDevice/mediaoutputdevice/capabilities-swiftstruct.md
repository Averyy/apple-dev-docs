# MediaOutputDevice.Capabilities

**Framework**: Media Device  
**Kind**: struct

Defines the media capabilities supported by a [`MediaOutputDevice`](mediaoutputdevice.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Capabilities
```

#### Overview

Use these options to describe what a device can do, such as streaming audio or video in realtime, playing media from a URL, or launching a remote application.

## Topics

### Instance Properties
- [var description: String](mediaoutputdevice/capabilities-swift.struct/description.md)
  A textual representation of the capabilities.
### Type Properties
- [static let appLaunch: MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct/applaunch.md)
  Capable of launching an application and providing an application-to-application data channel.
- [static let realtimeAudioStreaming: MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct/realtimeaudiostreaming.md)
  Capable of receiving audio samples and processing them in realtime.
- [static let realtimeVideoStreaming: MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct/realtimevideostreaming.md)
  Capable of receiving video samples and processing them in realtime.
- [static let urlPlayback: MediaOutputDevice.Capabilities](mediaoutputdevice/capabilities-swift.struct/urlplayback.md)
  Capable of receiving a media URL and providing a playback experience.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct MediaOutputDevice](mediaoutputdevice.md)
  Represents a discoverable media output device such as a TV, speaker, or streaming stick.
- [MediaOutputDevice.DeviceType](mediaoutputdevice/devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](mediaoutputdevice/volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.
- [MediaOutputDevice.AuthorizationMethod](mediaoutputdevice/authorizationmethod.md)
  Specifies what kind of authorization UI to present when connecting to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/capabilities-swift.struct)*