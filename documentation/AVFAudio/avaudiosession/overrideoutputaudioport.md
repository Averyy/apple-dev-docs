# overrideOutputAudioPort(_:)

**Framework**: AVFAudio  
**Kind**: method

Temporarily changes the current audio route.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func overrideOutputAudioPort(_ portOverride: AVAudioSession.PortOverride) throws
```

#### Discussion

If your app uses the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category, calling this method with the [`AVAudioSession.PortOverride.speaker`](avaudiosession/portoverride/speaker.md) option causes the system to route audio to the built-in speaker and microphone regardless of other settings. This change remains in effect only until the current route changes or you call this method again with the [`AVAudioSession.PortOverride.none`](avaudiosession/portoverride/none.md) option.

If you’d prefer to permanently enable this behavior, you should instead set the category’s [`defaultToSpeaker`](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md) option. Setting this option routes to the speaker rather than the receiver if no other accessory such as headphones are in use.

> **Note**:  The preferred method for routing audio to the speaker instead of the receiver for speakerphone functionality is through the use of the [`Media Player`](https://developer.apple.com/documentation/MediaPlayer) framework’s [`MPVolumeView`](https://developer.apple.com/documentation/MediaPlayer/MPVolumeView) class.

## Parameters

- `portOverride`: The override option for audio output. For a list of constants, see  .

## Topics

### Data Types
- [AVAudioSession.PortOverride](avaudiosession/portoverride.md)
  Constants for use with the [`overrideOutputAudioPort(_:)`](avaudiosession/overrideoutputaudioport(_:).md) method.

## See Also

- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/outputdatasources.md)
  An array of available output data sources for the current audio route.
- [var outputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/outputdatasource.md)
  The currently selected output data source.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setoutputdatasource(_:).md)
  Sets the output data source for an audio session.
- [class AVAudioSessionDataSourceDescription](avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/overrideoutputaudioport(_:))*