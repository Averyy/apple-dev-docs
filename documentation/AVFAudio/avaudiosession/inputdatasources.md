# inputDataSources

**Framework**: AVFAudio  
**Kind**: property

An array of available data sources for the audio session’s current input port.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var inputDataSources: [AVAudioSessionDataSourceDescription]? { get }
```

#### Discussion

This property returns an array of [`AVAudioSessionDataSourceDescription`](avaudiosessiondatasourcedescription.md) objects representing available input sources, or `nil` if switching between multiple input sources isn’t currently possible. Only certain devices and peripherals, such as an iPhone equipped with both front- and rear-facing microphones, support this feature.

You can observe changes to the value of this property by using key-value observing.

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
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setinputdatasource(_:).md)
  Selects a data source for the audio session’s current input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputdatasources)*