# availableInputsChangeNotification

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class let availableInputsChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVAudioSessionAvailableInputsChangeNotification;
```

#### Discussion

Notification sent to registered listeners when there are changes in [`availableInputs`](./availableinputs.md).

There is no payload (userInfo dictionary) associated with the [`availableInputsChangeNotification`](./availableinputschangenotification.md) notification.

## See Also

### Configuring inputs
- [var isInputAvailable: Bool](./isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](./availableinputs.md)
  An array of input ports available for audio routing.
- [var preferredInput: AVAudioSessionPortDescription?](./preferredinput.md)
  The preferred input port for audio routing.
- [func setPreferredInput(AVAudioSessionPortDescription?) throws](./setpreferredinput%28_%29.md)
  Sets the preferred input port for audio routing.
- [var inputDataSource: AVAudioSessionDataSourceDescription?](./inputdatasource.md)
  The currently selected input data source.
- [var inputDataSources: [AVAudioSessionDataSourceDescription]?](./inputdatasources.md)
  An array of available data sources for the audio session’s current input port.
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](./setinputdatasource%28_%29.md)
  Selects a data source for the audio session’s current input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availableinputschangenotification)*