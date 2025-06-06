# kMEVideoDecoderClassImplementationIDKey

**Framework**: MediaExtension  
**Kind**: var

The unique identifier for the video decoder.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEVideoDecoderClassImplementationIDKey: String { get }
```

#### Discussion

Format the string similar to the bundle identifier of the video decoder. Start with the reverse domain identifier of your developer account, followed by `.videodecoder.` and the name of the codec. If you plan to create multiple variants of the same video decoder, include an additional component to make each video decoder identifier unique; for example `com.mycompany.videodecoder.mycodec.codecvariant`.

## See Also

- [var kMERAWProcessorExtensionPointName: String](kmerawprocessorextensionpointname.md)
  The extension point name for RAW processors.
- [var kMEVideoDecoderObjectNameKey: String](kmevideodecoderobjectnamekey.md)
  A user-readable string describing the decoder.
- [var kMEVideoDecoderCodecInfoKey: String](kmevideodecodercodecinfokey.md)
  An array of one or more dictionaries describing the codecs that the decoder supports.
- [var kMEVideoDecoderCodecTypeKey: String](kmevideodecodercodectypekey.md)
  A string describing the four-character code of the codec that the decoder supports.
- [var kMEVideoDecoderCodecNameKey: String](kmevideodecodercodecnamekey.md)
  A user-readable string describing the name of the codec format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmevideodecoderclassimplementationidkey)*