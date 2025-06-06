# downmix

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the framework mixes the channels instead of remapping.

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
var downmix: Bool { get set }
```

#### Discussion

This property defaults to `false`, indicating that the framework remaps the channels. When `true`, and channel remapping is necessary, the framework mixes the channels.

## See Also

- [var channelMap: [NSNumber]](avaudioconverter/channelmap.md)
  An array of integers that indicates which input to derive each output from.
- [var dither: Bool](avaudioconverter/dither.md)
  A Boolean value that indicates whether dither is on.
- [var inputFormat: AVAudioFormat](avaudioconverter/inputformat.md)
  The format of the input audio stream.
- [var outputFormat: AVAudioFormat](avaudioconverter/outputformat.md)
  The format of the output audio stream.
- [var magicCookie: Data?](avaudioconverter/magiccookie.md)
  An object that contains metadata for encoders and decoders.
- [var maximumOutputPacketSize: Int](avaudioconverter/maximumoutputpacketsize.md)
  The maximum size of an output packet, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/downmix)*