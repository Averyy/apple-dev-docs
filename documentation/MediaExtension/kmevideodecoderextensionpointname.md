# kMEVideoDecoderExtensionPointName

**Framework**: MediaExtension  
**Kind**: var

The extension point name for video decoders.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEVideoDecoderExtensionPointName: String { get }
```

#### Discussion

The value for this string is `com.apple.mediaextension.videodecoder`.

## See Also

- [var kMEVideoDecoderClassImplementationIDKey: String](kmevideodecoderclassimplementationidkey.md)
  The unique identifier for the video decoder.
- [var kMEVideoDecoderObjectNameKey: String](kmevideodecoderobjectnamekey.md)
  A user-readable string describing the decoder.
- [var kMEVideoDecoderCodecInfoKey: String](kmevideodecodercodecinfokey.md)
  An array of one or more dictionaries describing the codecs that the decoder supports.
- [var kMEVideoDecoderCodecTypeKey: String](kmevideodecodercodectypekey.md)
  A string describing the four-character code of the codec that the decoder supports.
- [var kMEVideoDecoderCodecNameKey: String](kmevideodecodercodecnamekey.md)
  A user-readable string describing the name of the codec format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmevideodecoderextensionpointname)*