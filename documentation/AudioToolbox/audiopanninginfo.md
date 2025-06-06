# AudioPanningInfo

**Framework**: Audio Toolbox  
**Kind**: struct

Audio panning information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioPanningInfo
```

## Topics

### Initializers
- [init(mPanningMode: AudioPanningMode, mCoordinateFlags: UInt32, mCoordinates: (Float32, Float32, Float32), mGainScale: Float32, mOutputChannelMap: UnsafePointer<AudioChannelLayout>)](audiopanninginfo/init(mpanningmode:mcoordinateflags:mcoordinates:mgainscale:moutputchannelmap:).md)
### Instance Properties
- [var mCoordinateFlags: UInt32](audiopanninginfo/mcoordinateflags.md)
  For the available coordinate flags, see Channel Coordinate Flags.
- [var mCoordinates: (Float32, Float32, Float32)](audiopanninginfo/mcoordinates.md)
  For the available coordinate index constants, see Channel Coordinate Index Constants.
- [var mGainScale: Float32](audiopanninginfo/mgainscale.md)
  A multiplier for audio panning values, typically representing a volume value in the range from 0 to 1. A value of 1 results in audio panning at unity gain. A value of 0 silences all channels.
- [var mOutputChannelMap: UnsafePointer<AudioChannelLayout>](audiopanninginfo/moutputchannelmap.md)
  The channel map used to determine channel volumes for the audio panning.
- [var mPanningMode: AudioPanningMode](audiopanninginfo/mpanningmode.md)
  The mode to use for panning.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioBalanceFade](audiobalancefade.md)
  Describes audio left/right balance and front/back fade values.
- [struct AudioFormatInfo](audioformatinfo.md)
  A structure that specifies an audio format.
- [struct AudioFormatListItem](../CoreAudioTypes/AudioFormatListItem.md)
- [struct ExtendedAudioFormatInfo](extendedaudioformatinfo.md)
  A specifier for the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property, including the codec to use.
- [typealias AudioFormatPropertyID](audioformatpropertyid.md)
  A type for four-char codes for audio format property identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiopanninginfo)*