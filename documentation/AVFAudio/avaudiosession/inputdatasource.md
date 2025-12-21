# inputDataSource

**Framework**: AVFAudio  
**Kind**: property

The currently selected input data source.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var inputDataSource: AVAudioSessionDataSourceDescription? { get }
```

#### Discussion

The value of this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if switching between multiple input sources isn’t currently possible. Only certain devices and peripherals, such as an iPhone equipped with both front- and rear-facing microphones, support this feature.

## See Also

- [var isInputAvailable: Bool](avaudiosession/isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](avaudiosession/availableinputs.md)
  An array of input ports available for audio routing.
- [var preferredInput: AVAudioSessionPortDescription?](avaudiosession/preferredinput.md)
  The preferred input port for audio routing.
- [func setPreferredInput(AVAudioSessionPortDescription?) throws](avaudiosession/setpreferredinput(_:).md)
  Sets the preferred input port for audio routing.
- [var inputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/inputdatasources.md)
  An array of available data sources for the audio session’s current input port.
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setinputdatasource(_:).md)
  Selects a data source for the audio session’s current input port.
- [class let availableInputsChangeNotification: NSNotification.Name](avaudiosession/availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputdatasource)*