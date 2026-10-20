# preferredInput

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) AVAudioSessionPortDescription * preferredInput;
```

#### Discussion

The value of this property indicates the input port selected using the [`setPreferredInput(_:)`](./setpreferredinput%28_%29.md) method. To see the actual current input port, use the [`currentRoute`](./currentroute.md) property. This property returns [`nil`](../../ObjectiveC/nil-227m0.md) if you haven’t set a preference or if the previously set preferred input is no longer available.

## See Also

### Configuring inputs
- [var isInputAvailable: Bool](./isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](./availableinputs.md)
  An array of input ports available for audio routing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredinput)*