# outputDataSource

**Framework**: AVFAudio  
**Kind**: property

The currently selected output data source.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputDataSource: AVAudioSessionDataSourceDescription? { get }
```

#### Discussion

The value of this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if switching between multiple output sources isn’t currently possible. Only certain USB accessories support switching output sources.

## See Also

- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/outputdatasources.md)
  An array of available output data sources for the current audio route.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setoutputdatasource(_:).md)
  Sets the output data source for an audio session.
- [class AVAudioSessionDataSourceDescription](avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](avaudiosession/overrideoutputaudioport(_:).md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputdatasource)*