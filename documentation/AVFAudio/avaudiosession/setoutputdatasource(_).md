# setOutputDataSource(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setOutputDataSource:(AVAudioSessionDataSourceDescription *) dataSource error:(NSError **) outError;
```

#### Discussion

You can change the output source to one of the [`AVAudioSessionDataSourceDescription`](../avaudiosessiondatasourcedescription.md) objects in the [`outputDataSources`](./outputdatasources.md) array. Only certain USB accessories support this feature.

## Parameters

- `dataSource`: The data source for the audio session’s output.

## See Also

### Configuring outputs
- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](./outputdatasources.md)
  An array of available output data sources for the current audio route.
- [var outputDataSource: AVAudioSessionDataSourceDescription?](./outputdatasource.md)
  The currently selected output data source.
- [class AVAudioSessionDataSourceDescription](../avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](./overrideoutputaudioport%28_%29.md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setoutputdatasource(_:))*