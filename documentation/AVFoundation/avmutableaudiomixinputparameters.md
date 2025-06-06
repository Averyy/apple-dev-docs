# AVMutableAudioMixInputParameters

**Framework**: AVFoundation  
**Kind**: class

The parameters you use when adding an audio track to a mix.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMutableAudioMixInputParameters
```

## Topics

### Creating Input Parameters
- [convenience init(track: AVAssetTrack?)](avmutableaudiomixinputparameters/init(track:).md)
  Creates a mutable input parameters object for a given track.
### Managing the Track ID
- [var trackID: CMPersistentTrackID](avmutableaudiomixinputparameters/trackid.md)
  The identifier of the audio track to which the parameters should be applied.
### Setting the Volume
- [func setVolume(Float, at: CMTime)](avmutableaudiomixinputparameters/setvolume(_:at:).md)
  Sets the value of the audio volume starting at the specified time.
- [func setVolumeRamp(fromStartVolume: Float, toEndVolume: Float, timeRange: CMTimeRange)](avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume:toendvolume:timerange:).md)
  Sets a volume ramp to apply during a specified time range.
### Getting an Audio Tap
- [var audioTapProcessor: MTAudioProcessingTap?](avmutableaudiomixinputparameters/audiotapprocessor.md)
  The audio processing tap associated with the track.
### Time Pitch Settings
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm?](avmutableaudiomixinputparameters/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch for scaled audio edits.
- [struct AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md)
  An algorithm used to set the audio pitch as the rate changes.

## Relationships

### Inherits From
- [AVAudioMixInputParameters](avaudiomixinputparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioMix](avaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVMutableAudioMix](avmutableaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVAudioMixInputParameters](avaudiomixinputparameters.md)
  An object that represents the parameters that you apply when adding an audio track to a mix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters)*