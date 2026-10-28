# dither

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether dither is on.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var dither: Bool { get set }
```

```objc
@property (nonatomic) BOOL dither;
```

## Discussion

This property defaults to `false`. When `true`, the framework determines whether dithering makes sense for the formats and settings.

## See Also

### Getting audio converter properties
- [var channelMap: [NSNumber]](./channelmap.md)
  An array of integers that indicates which input to derive each output from.
- [var downmix: Bool](./downmix.md)
  A Boolean value that indicates whether the framework mixes the channels instead of remapping.
- [var inputFormat: AVAudioFormat](./inputformat.md)
  The format of the input audio stream.
- [var outputFormat: AVAudioFormat](./outputformat.md)
  The format of the output audio stream.
- [var magicCookie: Data?](./magiccookie.md)
  An object that contains metadata for encoders and decoders.
- [var maximumOutputPacketSize: Int](./maximumoutputpacketsize.md)
  The maximum size of an output packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/dither)*