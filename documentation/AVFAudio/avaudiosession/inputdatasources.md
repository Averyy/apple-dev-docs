# inputDataSources

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> * inputDataSources;
```

## Discussion

This property returns an array of [`AVAudioSessionDataSourceDescription`](../avaudiosessiondatasourcedescription.md) objects representing available input sources, or `nil` if switching between multiple input sources isn’t currently possible. Only certain devices and peripherals, such as an iPhone equipped with both front- and rear-facing microphones, support this feature.

You can observe changes to the value of this property by using key-value observing.

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
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](./setinputdatasource%28_%29.md)
  Selects a data source for the audio session’s current input port.
- [class let availableInputsChangeNotification: NSNotification.Name](./availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputdatasources)*