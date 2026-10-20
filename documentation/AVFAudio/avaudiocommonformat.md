# AVAudioCommonFormat

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The format options that describe common audio formats.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVAudioCommonFormat
```

```c
enum AVAudioCommonFormat : NSUInteger;
```

## Topics

### Creating a common format
- [init?(rawValue: UInt)](./avaudiocommonformat/init%28rawvalue%29.md)
### Choosing a sample format
- [AVAudioCommonFormat.otherFormat](./avaudiocommonformat/otherformat.md)
  A format other than one the enumeration specifies.
- [AVAudioCommonFormat.pcmFormatFloat32](./avaudiocommonformat/pcmformatfloat32.md)
  A format that represents the standard format as native-endian floats.
- [AVAudioCommonFormat.pcmFormatFloat64](./avaudiocommonformat/pcmformatfloat64.md)
  A format that represents native-endian doubles.
- [AVAudioCommonFormat.pcmFormatInt16](./avaudiocommonformat/pcmformatint16.md)
  A format that represents signed 16-bit native-endian integers.
- [AVAudioCommonFormat.pcmFormatInt32](./avaudiocommonformat/pcmformatint32.md)
  A format that represents signed 32-bit native-endian integers.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining the audio format
- [var isInterleaved: Bool](./avaudioformat/isinterleaved.md)
  A Boolean value that indicates whether the samples mix into one stream.
- [var isStandard: Bool](./avaudioformat/isstandard.md)
  A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [var commonFormat: AVAudioCommonFormat](./avaudioformat/commonformat.md)
  The common format identifier instance.
- [var settings: [String : Any]](./avaudioformat/settings.md)
  A dictionary that represents the format as a dictionary using audio setting keys.
- [var magicCookie: Data?](./avaudioformat/magiccookie.md)
  An object that contains metadata that encoders and decoders require.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocommonformat)*