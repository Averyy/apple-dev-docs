# setInputDataSource(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Selects a data source for the audio session’s current input port.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws
```

```objc
- (BOOL) setInputDataSource:(AVAudioSessionDataSourceDescription *) dataSource error:(NSError **) outError;
```

#### Discussion

You can set the input source to exactly one of the [`AVAudioSessionDataSourceDescription`](../avaudiosessiondatasourcedescription.md) objects in the [`inputDataSources`](./inputdatasources.md) array. Only certain devices and peripherals, such as an iPhone equipped with both front- and rear-facing microphones, support switching among input sources.

## Parameters

- `dataSource`: The data source for the audio session’s input.

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
- [class let availableInputsChangeNotification: NSNotification.Name](./availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setinputdatasource(_:))*