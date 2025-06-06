# AudioFormatInfo

**Framework**: Audio Toolbox  
**Kind**: struct

A structure that specifies an audio format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFormatInfo
```

#### Overview

Use this value with the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property.

## Topics

### Initializers
- [init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafeRawPointer, mMagicCookieSize: UInt32)](audioformatinfo/init(masbd:mmagiccookie:mmagiccookiesize:).md)
### Instance Properties
- [var mASBD: AudioStreamBasicDescription](audioformatinfo/masbd.md)
  An `AudioStreamBasicDescription` structure.
- [var mMagicCookie: UnsafeRawPointer](audioformatinfo/mmagiccookie.md)
  A pointer to the decompression information for the data described in the `mASBD` parameter.
- [var mMagicCookieSize: UInt32](audioformatinfo/mmagiccookiesize.md)
  The size, in bytes, of the `mMagicCookie` parameter.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioBalanceFade](audiobalancefade.md)
  Describes audio left/right balance and front/back fade values.
- [struct AudioFormatListItem](../CoreAudioTypes/AudioFormatListItem.md)
- [struct AudioPanningInfo](audiopanninginfo.md)
  Audio panning information.
- [struct ExtendedAudioFormatInfo](extendedaudioformatinfo.md)
  A specifier for the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property, including the codec to use.
- [typealias AudioFormatPropertyID](audioformatpropertyid.md)
  A type for four-char codes for audio format property identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioformatinfo)*