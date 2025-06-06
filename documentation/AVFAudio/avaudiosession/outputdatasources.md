# outputDataSources

**Framework**: AVFAudio  
**Kind**: property

An array of available output data sources for the current audio route.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputDataSources: [AVAudioSessionDataSourceDescription]? { get }
```

#### Discussion

This property returns an array of [`AVAudioSessionDataSourceDescription`](avaudiosessiondatasourcedescription.md) objects representing available output sources, or `nil` if switching between multiple output sources isn’t currently possible. Only certain USB accessories support this feature.

You can observe changes to the value of this property by using key-value observing.

## See Also

- [var outputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/outputdatasource.md)
  The currently selected output data source.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setoutputdatasource(_:).md)
  Sets the output data source for an audio session.
- [class AVAudioSessionDataSourceDescription](avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](avaudiosession/overrideoutputaudioport(_:).md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputdatasources)*