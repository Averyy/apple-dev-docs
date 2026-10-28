# availableInputs

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of input ports available for audio routing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var availableInputs: [AVAudioSessionPortDescription]? { get }
```

```objc
@property (readonly, nullable) NSArray<AVAudioSessionPortDescription *> * availableInputs;
```

## Discussion

The active audio session category and mode determine the number of inputs this property returns. For example, if the session’s category is [`playAndRecord`](./category-swift.struct/playandrecord.md), the array may contain a built-in microphone port and, if connected, a headset microphone port. Alternatively, if the session’s category is [`playback`](./category-swift.struct/playback.md), this property returns an empty array.

## See Also

### Configuring inputs
- [var isInputAvailable: Bool](./isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
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
- [class let availableInputsChangeNotification: NSNotification.Name](./availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availableinputs)*