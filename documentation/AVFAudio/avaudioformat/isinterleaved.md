# isInterleaved

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the samples mix into one stream.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isInterleaved: Bool { get }
```

#### Discussion

This value is only valid for PCM formats.

## See Also

- [var isStandard: Bool](avaudioformat/isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](avaudioformat/commonformat.md)
  The common format identifier instance.
- [var settings: [String : Any]](avaudioformat/settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.
- [var magicCookie: Data?](avaudioformat/magiccookie.md)
  An object that contains metadata that encoders and decoders require.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/isinterleaved)*