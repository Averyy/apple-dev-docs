# ExtendedAudioFormatInfo

**Framework**: Audio Toolbox  
**Kind**: struct

A specifier for the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property, including the codec to use.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct ExtendedAudioFormatInfo
```

## Topics

### Initializers
- [init()](extendedaudioformatinfo/init.md)
- [init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafeRawPointer?, mMagicCookieSize: UInt32, mClassDescription: AudioClassDescription)](extendedaudioformatinfo/init(masbd:mmagiccookie:mmagiccookiesize:mclassdescription:).md)
### Instance Properties
- [var mASBD: AudioStreamBasicDescription](extendedaudioformatinfo/masbd.md)
  A format specification for an audio stream.
- [var mClassDescription: AudioClassDescription](extendedaudioformatinfo/mclassdescription.md)
  A structure that describes an audio codec.
- [var mMagicCookie: UnsafeRawPointer?](extendedaudioformatinfo/mmagiccookie.md)
  Decompression information for the audio data format specified in the `mASBD` field.
- [var mMagicCookieSize: UInt32](extendedaudioformatinfo/mmagiccookiesize.md)
  The size, in bytes, of the `mMagicCookie` field.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioBalanceFade](audiobalancefade.md)
  Describes audio left/right balance and front/back fade values.
- [struct AudioFormatInfo](audioformatinfo.md)
  A structure that specifies an audio format.
- [struct AudioFormatListItem](../CoreAudioTypes/AudioFormatListItem.md)
- [struct AudioPanningInfo](audiopanninginfo.md)
  Audio panning information.
- [typealias AudioFormatPropertyID](audioformatpropertyid.md)
  A type for four-char codes for audio format property identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo)*