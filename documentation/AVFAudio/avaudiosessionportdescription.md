# AVAudioSessionPortDescription

**Framework**: AVFAudio  
**Kind**: class

Information about the capabilities of the port and the hardware channels it supports.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioSessionPortDescription
```

#### Overview

A port description object describes a single input or output port associated with an audio route. Examples of audio ports include a device’s built-in speaker, a microphone on a wired headset, and a Bluetooth device supporting the Advanced Audio Distribution Profile (A2DP).

You can query the audio session’s [`currentRoute`](avaudiosession/currentroute.md) property to get information about the active set of input and output ports. To change the current audio routing, call the [`setPreferredInput(_:)`](avaudiosession/setpreferredinput(_:).md) method. For example, on a device with a wired headset attached, the audio session’s [`availableInputs`](avaudiosession/availableinputs.md) array may contain two port descriptions: one for the headset microphone and one for the device’s built-in microphone. You can use the audio session’s [`setPreferredInput(_:)`](avaudiosession/setpreferredinput(_:).md) method to select the headset or built-in microphone for audio input.

## Topics

### Getting the Port Attributes
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
- [var isSpatialAudioEnabled: Bool](avaudiosessionportdescription/isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.
### Managing a Port’s Data Sources
- [var dataSources: [AVAudioSessionDataSourceDescription]?](avaudiosessionportdescription/datasources.md)
  The available data sources for the port.
- [var selectedDataSource: AVAudioSessionDataSourceDescription?](avaudiosessionportdescription/selecteddatasource.md)
  The currently selected audio data source for the port.
- [var preferredDataSource: AVAudioSessionDataSourceDescription?](avaudiosessionportdescription/preferreddatasource.md)
  The preferred audio data source for the port.
- [func setPreferredDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosessionportdescription/setpreferreddatasource(_:).md)
  Sets the preferred audio data source for the port.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var currentRoute: AVAudioSessionRouteDescription](avaudiosession/currentroute.md)
  A description of the current audio route’s input and output ports.
- [class AVAudioSessionRouteDescription](avaudiosessionroutedescription.md)
  An object that describes the input and output ports associated with a session’s audio route.
- [class let routeChangeNotification: NSNotification.Name](avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription)*