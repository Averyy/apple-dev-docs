# magicCookie

**Framework**: AVFAudio  
**Kind**: property

An object that contains metadata that encoders and decoders require.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var magicCookie: Data? { get set }
```

#### Discussion

Encoders produce a `magicCookie` object, and some decoders require it to decode properly.

## See Also

- [var isInterleaved: Bool](avaudioformat/isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var isStandard: Bool](avaudioformat/isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](avaudioformat/commonformat.md)
  The common format identifier instance.
- [var settings: [String : Any]](avaudioformat/settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/magiccookie)*