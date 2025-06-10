# sourceFormatHint

**Framework**: AVFoundation  
**Kind**: property

A hint about the format of the sample buffers to append to the input.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceFormatHint: CMFormatDescription? { get }
```

#### Discussion

An input may use this hint to fill in missing output settings or perform additional upfront validation of samples.

> **Note**:  To ensure successful file writing when you initialize an input with a source format hint, only append samples of this type.

## See Also

- [var mediaType: AVMediaType](avassetwriterinput/mediatype.md)
  The media type of the samples that the input accepts.
- [var outputSettings: [String : Any]?](avassetwriterinput/outputsettings.md)
  The settings to use for encoding media data you append to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/sourceformathint)*