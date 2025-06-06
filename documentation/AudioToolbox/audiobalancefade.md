# AudioBalanceFade

**Framework**: Audio Toolbox  
**Kind**: struct

Describes audio left/right balance and front/back fade values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioBalanceFade
```

#### Overview

This data structure is used with the [`kAudioFormatProperty_BalanceFade`](kaudioformatproperty_balancefade.md) property.

## Topics

### Initializers
- [init(mLeftRightBalance: Float32, mBackFrontFade: Float32, mType: AudioBalanceFadeType, mChannelLayout: UnsafePointer<AudioChannelLayout>)](audiobalancefade/init(mleftrightbalance:mbackfrontfade:mtype:mchannellayout:).md)
### Instance Properties
- [var mBackFrontFade: Float32](audiobalancefade/mbackfrontfade.md)
  The audio front/back fade, where -1 represents full rear, 0 represents center, and +1 represents full front.
- [var mChannelLayout: UnsafePointer<AudioChannelLayout>](audiobalancefade/mchannellayout.md)
  The size, in bytes, of the `mMagicCookie` parameter.
- [var mLeftRightBalance: Float32](audiobalancefade/mleftrightbalance.md)
  The audio left/right balance, where -1 represents full left, 0 represents center, and +1 represents full right.
- [var mType: AudioBalanceFadeType](audiobalancefade/mtype.md)
  An AudioBalanceFadeType constant. max unity gain, or equal power.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioFormatInfo](audioformatinfo.md)
  A structure that specifies an audio format.
- [struct AudioFormatListItem](../CoreAudioTypes/AudioFormatListItem.md)
- [struct AudioPanningInfo](audiopanninginfo.md)
  Audio panning information.
- [struct ExtendedAudioFormatInfo](extendedaudioformatinfo.md)
  A specifier for the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property, including the codec to use.
- [typealias AudioFormatPropertyID](audioformatpropertyid.md)
  A type for four-char codes for audio format property identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiobalancefade)*