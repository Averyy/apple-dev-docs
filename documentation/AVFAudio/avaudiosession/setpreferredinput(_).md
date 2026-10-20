# setPreferredInput(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred input port for audio routing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredInput(_ inPort: AVAudioSessionPortDescription?) throws
```

```objc
- (BOOL) setPreferredInput:(AVAudioSessionPortDescription *) inPort error:(NSError **) outError;
```

#### Discussion

Setting the preferred input port requests a change to the input audio route. To determine whether the change has taken effect, use the [`currentRoute`](./currentroute.md) property.

The value of the `inPort` parameter must be one of the [`AVAudioSessionPortDescription`](../avaudiosessionportdescription.md) objects in the [`availableInputs`](./availableinputs.md) array. If this parameter specifies a port that isn’t already part of the current audio route and the app’s session controls audio routing, this method initiates a route change to use the preferred port.

You must set a preferred input port only after setting the audio session’s category and mode and activating the session.

## Parameters

- `inPort`: An [`AVAudioSessionPortDescription`](../avaudiosessionportdescription.md) object that describes the port to use for input.

## See Also

### Configuring inputs
- [var isInputAvailable: Bool](./isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](./availableinputs.md)
  An array of input ports available for audio routing.
- [var preferredInput: AVAudioSessionPortDescription?](./preferredinput.md)
  The preferred input port for audio routing.
- [var inputDataSource: AVAudioSessionDataSourceDescription?](./inputdatasource.md)
  The currently selected input data source.
- [var inputDataSources: [AVAudioSessionDataSourceDescription]?](./inputdatasources.md)
  An array of available data sources for the audio session’s current input port.
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](./setinputdatasource%28_%29.md)
  Selects a data source for the audio session’s current input port.
- [class let availableInputsChangeNotification: NSNotification.Name](./availableinputschangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredinput(_:))*