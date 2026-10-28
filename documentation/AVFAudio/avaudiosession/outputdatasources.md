# outputDataSources

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> * outputDataSources;
```

## Discussion

This property returns an array of [`AVAudioSessionDataSourceDescription`](../avaudiosessiondatasourcedescription.md) objects representing available output sources, or `nil` if switching between multiple output sources isn’t currently possible. Only certain USB accessories support this feature.

You can observe changes to the value of this property by using key-value observing.

## See Also

### Configuring outputs
- [var outputDataSource: AVAudioSessionDataSourceDescription?](./outputdatasource.md)
  The currently selected output data source.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](./setoutputdatasource%28_%29.md)
  Sets the output data source for an audio session.
- [class AVAudioSessionDataSourceDescription](../avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](./overrideoutputaudioport%28_%29.md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputdatasources)*