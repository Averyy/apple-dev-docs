# isInputAvailable

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isInputAvailable) BOOL inputAvailable;
```

#### Return Value

[`true`](../../Swift/true.md) if an input route is available, otherwise [`false`](../../Swift/false.md).

#### Discussion

Use this property to determine whether the device currently supports audio input.

This property is key-value observable.

## See Also

### Configuring inputs
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
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](./setinputdatasource%28_%29.md)
  Selects a data source for the audio session’s current input port.
- [class let availableInputsChangeNotification: NSNotification.Name](./availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isinputavailable)*