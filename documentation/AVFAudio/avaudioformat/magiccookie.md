# magicCookie

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, nullable) NSData * magicCookie;
```

#### Discussion

Encoders produce a `magicCookie` object, and some decoders require it to decode properly.

## See Also

### Determining the audio format
- [var isInterleaved: Bool](./isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var isStandard: Bool](./isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](./commonformat.md)
  The common format identifier instance.
- [enum AVAudioCommonFormat](../avaudiocommonformat.md)
  The format options that describe common audio formats.
- [var settings: [String : Any]](./settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/magiccookie)*