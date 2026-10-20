# isSpatialAudioEnabled

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isSpatialAudioEnabled) BOOL spatialAudioEnabled;
```

#### Discussion

This property is only relevant in the context of ports that have a small number of hardware channels (typically 2), but have enhanced capabilities for playing multichannel content.

When you create a “Now Playing” app, inform the system if the app supports multichannel audio content by using [`setSupportsMultichannelContent(_:)`](../avaudiosession/setsupportsmultichannelcontent%28_%29.md). To detect changes in user preferences that affect spatial audio playback, register to receive the notification by using [`spatialPlaybackCapabilitiesChangedNotification`](../avaudiosession/spatialplaybackcapabilitieschangednotification.md).

Some port types — like USB and HDMI — may support multichannel playback because they have hardware formats supporting more than 2 channels. For example, many HDMI receivers connect to many speakers and are capable of rendering 5.1, 7.1, or other popular surround sound formats. Use [`setPreferredOutputNumberOfChannels(_:)`](../avaudiosession/setpreferredoutputnumberofchannels%28_%29.md) to set the preferred number of hardware channels, and query the number of channels by using [`maximumOutputNumberOfChannels`](../avaudiosession/maximumoutputnumberofchannels.md).

For more information about “Now Playing” apps, see [Becoming a now playable app](../../MediaPlayer/becoming-a-now-playable-app.md).

## See Also

### Getting the port attributes
- [var portName: String](./portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](./porttype.md)
  The type of the port.
- [AVAudioSession.Port](../avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [var channels: [AVAudioSessionChannelDescription]?](./channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](../avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](./uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](./hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/isspatialaudioenabled)*