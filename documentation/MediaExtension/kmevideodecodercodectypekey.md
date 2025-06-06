# kMEVideoDecoderCodecTypeKey

**Framework**: MediaExtension  
**Kind**: var

A string describing the four-character code of the codec that the decoder supports.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEVideoDecoderCodecTypeKey: String { get }
```

#### Discussion

This string should be exactly four characters long and use ASCII character set encoding.

## See Also

- [var kMEVideoDecoderClassImplementationIDKey: String](kmevideodecoderclassimplementationidkey.md)
  The unique identifier for the video decoder.
- [var kMERAWProcessorExtensionPointName: String](kmerawprocessorextensionpointname.md)
  The extension point name for RAW processors.
- [var kMEVideoDecoderObjectNameKey: String](kmevideodecoderobjectnamekey.md)
  A user-readable string describing the decoder.
- [var kMEVideoDecoderCodecInfoKey: String](kmevideodecodercodecinfokey.md)
  An array of one or more dictionaries describing the codecs that the decoder supports.
- [var kMEVideoDecoderCodecNameKey: String](kmevideodecodercodecnamekey.md)
  A user-readable string describing the name of the codec format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmevideodecodercodectypekey)*