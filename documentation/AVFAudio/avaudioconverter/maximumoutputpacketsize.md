# maximumOutputPacketSize

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The maximum size of an output packet, in bytes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var maximumOutputPacketSize: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger maximumOutputPacketSize;
```

## See Also

### Getting audio converter properties
- [var channelMap: [NSNumber]](./channelmap.md)
  An array of integers that indicates which input to derive each output from.
- [var dither: Bool](./dither.md)
  A Boolean value that indicates whether dither is on.
- [var downmix: Bool](./downmix.md)
  A Boolean value that indicates whether the framework mixes the channels instead of remapping.
- [var inputFormat: AVAudioFormat](./inputformat.md)
  The format of the input audio stream.
- [var outputFormat: AVAudioFormat](./outputformat.md)
  The format of the output audio stream.
- [var magicCookie: Data?](./magiccookie.md)
  An object that contains metadata for encoders and decoders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/maximumoutputpacketsize)*