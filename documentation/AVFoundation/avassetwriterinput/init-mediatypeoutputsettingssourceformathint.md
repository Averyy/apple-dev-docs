# init(mediaType:outputSettings:sourceFormatHint:)

**Framework**: AVFoundation  
**Kind**: init

Creates an input that appends sample buffers of the specified type and format hint to the output file.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(mediaType: AVMediaType, outputSettings: [String : Any]?, sourceFormatHint: CMFormatDescription?)
```

#### Discussion

To guarantee successful file writing, ensure that sample buffers you append are of the specified format.

## Parameters

- `mediaType`: The type of media that an input accepts.
- `outputSettings`: The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use   to create preset-based settings.
- `sourceFormatHint`: The system raises an error if the format description isn’t valid for the indicated media type.

## See Also

- [convenience init(mediaType: AVMediaType, outputSettings: [String : Any]?)](avassetwriterinput/init(mediatype:outputsettings:).md)
  Creates an input to append sample buffers of the specified type to the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:sourceformathint:))*