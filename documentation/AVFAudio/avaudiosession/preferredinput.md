# preferredInput

**Framework**: AVFAudio  
**Kind**: property

The preferred input port for audio routing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredInput: AVAudioSessionPortDescription? { get }
```

#### Discussion

The value of this property indicates the input port selected using the [`setPreferredInput(_:)`](avaudiosession/setpreferredinput(_:).md) method. To see the actual current input port, use the [`currentRoute`](avaudiosession/currentroute.md) property. This property returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if you haven’t set a preference or if the previously set preferred input is no longer available.

## See Also

- [var isInputAvailable: Bool](avaudiosession/isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](avaudiosession/availableinputs.md)
  An array of input ports available for audio routing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredinput)*