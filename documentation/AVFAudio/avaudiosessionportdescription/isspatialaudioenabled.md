# isSpatialAudioEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the port supports spatial audio playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isSpatialAudioEnabled: Bool { get }
```

#### Discussion

This property is only relevant in the context of ports that have a small number of hardware channels (typically 2), but have enhanced capabilities for playing multichannel content.

When you create a “Now Playing” app, inform the system if the app supports multichannel audio content by using [`setSupportsMultichannelContent(_:)`](avaudiosession/setsupportsmultichannelcontent(_:).md). To detect changes in user preferences that affect spatial audio playback, register to receive the notification by using [`spatialPlaybackCapabilitiesChangedNotification`](avaudiosession/spatialplaybackcapabilitieschangednotification.md).

Some port types — like USB and HDMI — may support multichannel playback because they have hardware formats supporting more than 2 channels. For example, many HDMI receivers connect to many speakers and are capable of rendering 5.1, 7.1, or other popular surround sound formats. Use [`setPreferredOutputNumberOfChannels(_:)`](avaudiosession/setpreferredoutputnumberofchannels(_:).md) to set the preferred number of hardware channels, and query the number of channels by using [`maximumOutputNumberOfChannels`](avaudiosession/maximumoutputnumberofchannels.md).

For more information about “Now Playing” apps, see [`Becoming a now playable app`](https://developer.apple.com/documentation/MediaPlayer/becoming-a-now-playable-app).

## See Also

- [var portName: String](avaudiosessionportdescription/portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](avaudiosessionportdescription/porttype.md)
  The type of the port.
- [AVAudioSession.Port](avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [var channels: [AVAudioSessionChannelDescription]?](avaudiosessionportdescription/channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](avaudiosessionportdescription/uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](avaudiosessionportdescription/hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/isspatialaudioenabled)*