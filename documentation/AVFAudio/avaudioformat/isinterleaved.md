# isInterleaved

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isInterleaved) BOOL interleaved;
```

## Discussion

This value is only valid for PCM formats.

## See Also

### Determining the audio format
- [var isStandard: Bool](./isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](./commonformat.md)
  The common format identifier instance.
- [enum AVAudioCommonFormat](../avaudiocommonformat.md)
  The format options that describe common audio formats.
- [var settings: [String : Any]](./settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.
- [var magicCookie: Data?](./magiccookie.md)
  An object that contains metadata that encoders and decoders require.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/isinterleaved)*