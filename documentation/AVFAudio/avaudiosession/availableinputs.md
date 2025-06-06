# availableInputs

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

The active audio session category and mode determine the number of inputs this property returns. For example, if the session’s category is [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), the array may contain a built-in microphone port and, if connected, a headset microphone port. Alternatively, if the session’s category is [`playback`](avaudiosession/category-swift.struct/playback.md), this property returns an empty array.

## See Also

- [var isInputAvailable: Bool](avaudiosession/isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/availableinputs)*