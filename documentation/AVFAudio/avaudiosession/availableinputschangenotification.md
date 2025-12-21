# availableInputsChangeNotification

**Framework**: AVFAudio  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class let availableInputsChangeNotification: NSNotification.Name
```

#### Discussion

Notification sent to registered listeners when there are changes in [`availableInputs`](avaudiosession/availableinputs.md).

There is no payload (userInfo dictionary) associated with the [`availableInputsChangeNotification`](avaudiosession/availableinputschangenotification.md) notification.

## See Also

- [var isInputAvailable: Bool](avaudiosession/isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](avaudiosession/availableinputs.md)
  An array of input ports available for audio routing.
- [var preferredInput: AVAudioSessionPortDescription?](avaudiosession/preferredinput.md)
  The preferred input port for audio routing.
- [func setPreferredInput(AVAudioSessionPortDescription?) throws](avaudiosession/setpreferredinput(_:).md)
  Sets the preferred input port for audio routing.
- [var inputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/inputdatasource.md)
  The currently selected input data source.
- [var inputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/inputdatasources.md)
  An array of available data sources for the audio session’s current input port.
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setinputdatasource(_:).md)
  Selects a data source for the audio session’s current input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availableinputschangenotification)*