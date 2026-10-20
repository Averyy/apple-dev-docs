# MediaOutputDevice.Capabilities

**Framework**: Media Device  
**Kind**: struct  
**Role**: Structure

Defines the media capabilities supported by a [`MediaOutputDevice`](../mediaoutputdevice.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct Capabilities
```

#### Overview

Use these options to describe what a device can do, such as streaming audio or video in realtime, playing media from a URL, or launching a remote application.

## Topics

### Instance Properties
- [var description: String](./capabilities-swift.struct/description.md)
  A textual representation of the capabilities.
### Type Properties
- [static let appLaunch: MediaOutputDevice.Capabilities](./capabilities-swift.struct/applaunch.md)
  Capable of launching an application and providing an application-to-application data channel.
- [static let realtimeAudioStreaming: MediaOutputDevice.Capabilities](./capabilities-swift.struct/realtimeaudiostreaming.md)
  Capable of receiving audio samples and processing them in realtime.
- [static let realtimeVideoStreaming: MediaOutputDevice.Capabilities](./capabilities-swift.struct/realtimevideostreaming.md)
  Capable of receiving video samples and processing them in realtime.
- [static let urlPlayback: MediaOutputDevice.Capabilities](./capabilities-swift.struct/urlplayback.md)
  Capable of receiving a media URL and providing a playback experience.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Device discovery and management
- [struct MediaOutputDevice](../mediaoutputdevice.md)
  Represents a discoverable media output device such as a TV, speaker, or streaming stick.
- [MediaOutputDevice.DeviceType](./devicetype-swift.enum.md)
  A device type used for display in user interfaces.
- [MediaOutputDevice.VolumeControl](./volumecontrol-swift.enum.md)
  Defines the type of volume control supported by an output device or group.
- [MediaOutputDevice.AuthorizationMethod](./authorizationmethod.md)
  Specifies what kind of authorization UI to present when connecting to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/capabilities-swift.struct)*