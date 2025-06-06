# setOutputDataSource(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the output data source for an audio session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws
```

#### Discussion

You can change the output source to one of the [`AVAudioSessionDataSourceDescription`](avaudiosessiondatasourcedescription.md) objects in the [`outputDataSources`](avaudiosession/outputdatasources.md) array. Only certain USB accessories support this feature.

## Parameters

- `dataSource`: The data source for the audio session’s output.

## See Also

- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/outputdatasources.md)
  An array of available output data sources for the current audio route.
- [var outputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/outputdatasource.md)
  The currently selected output data source.
- [class AVAudioSessionDataSourceDescription](avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](avaudiosession/overrideoutputaudioport(_:).md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setoutputdatasource(_:))*