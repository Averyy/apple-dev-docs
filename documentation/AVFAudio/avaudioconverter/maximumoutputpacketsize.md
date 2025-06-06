# maximumOutputPacketSize

**Framework**: AVFAudio  
**Kind**: property

The maximum size of an output packet, in bytes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var maximumOutputPacketSize: Int { get }
```

## See Also

- [var channelMap: [NSNumber]](avaudioconverter/channelmap.md)
  An array of integers that indicates which input to derive each output from.
- [var dither: Bool](avaudioconverter/dither.md)
  A Boolean value that indicates whether dither is on.
- [var downmix: Bool](avaudioconverter/downmix.md)
  A Boolean value that indicates whether the framework mixes the channels instead of remapping.
- [var inputFormat: AVAudioFormat](avaudioconverter/inputformat.md)
  The format of the input audio stream.
- [var outputFormat: AVAudioFormat](avaudioconverter/outputformat.md)
  The format of the output audio stream.
- [var magicCookie: Data?](avaudioconverter/magiccookie.md)
  An object that contains metadata for encoders and decoders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/maximumoutputpacketsize)*