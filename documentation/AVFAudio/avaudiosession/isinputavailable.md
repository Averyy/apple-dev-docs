# isInputAvailable

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether an audio input path is available.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isInputAvailable: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if an input route is available, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this property to determine whether the device currently supports audio input.

This property is key-value observable.

## See Also

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
- [class let availableInputsChangeNotification: NSNotification.Name](avaudiosession/availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isinputavailable)*