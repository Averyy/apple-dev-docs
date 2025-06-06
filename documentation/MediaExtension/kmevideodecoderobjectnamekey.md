# kMEVideoDecoderObjectNameKey

**Framework**: MediaExtension  
**Kind**: var

A user-readable string describing the decoder.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEVideoDecoderObjectNameKey: String { get }
```

#### Discussion

This string is used internally for uniquely identifying video decoders and possibly for debug logging but is typically not visible to users.

## See Also

- [var kMEVideoDecoderClassImplementationIDKey: String](kmevideodecoderclassimplementationidkey.md)
  The unique identifier for the video decoder.
- [var kMERAWProcessorExtensionPointName: String](kmerawprocessorextensionpointname.md)
  The extension point name for RAW processors.
- [var kMEVideoDecoderCodecInfoKey: String](kmevideodecodercodecinfokey.md)
  An array of one or more dictionaries describing the codecs that the decoder supports.
- [var kMEVideoDecoderCodecTypeKey: String](kmevideodecodercodectypekey.md)
  A string describing the four-character code of the codec that the decoder supports.
- [var kMEVideoDecoderCodecNameKey: String](kmevideodecodercodecnamekey.md)
  A user-readable string describing the name of the codec format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmevideodecoderobjectnamekey)*