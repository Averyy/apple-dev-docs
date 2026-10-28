# init(mediaType:outputSettings:sourceFormatHint:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithMediaType:(AVMediaType) mediaType outputSettings:(NSDictionary<NSString *,id> *) outputSettings sourceFormatHint:(CMFormatDescriptionRef) sourceFormatHint;
```

## Discussion

To guarantee successful file writing, ensure that sample buffers you append are of the specified format.

## Parameters

- `mediaType`: The type of media that an input accepts.
- `outputSettings`: The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use [`AVOutputSettingsAssistant`](../avoutputsettingsassistant.md) to create preset-based settings.
- `sourceFormatHint`: A hint about the format of the media data to append. The input uses the source format hint to fill in missing output settings. If you specify a hint, you only need to specify [`AVFormatIDKey`](../../AVFAudio/avformatidkey.md) for the audio output settings, and [`AVVideoCodecKey`](../avvideocodeckey.md) is the only required key for video output settings.

  The system raises an error if the format description isn’t valid for the indicated media type.

## See Also

### Creating an input
- [convenience init(mediaType: AVMediaType, outputSettings: [String : Any]?)](./init%28mediatype,outputsettings%29.md)
  Creates an input to append sample buffers of the specified type to the output file.
- [+ assetWriterInputWithMediaType:outputSettings:](./assetwriterinputwithmediatype_outputsettings_.md)
  Returns a new input to append sample buffers of the specified type to the output file.
- [+ assetWriterInputWithMediaType:outputSettings:sourceFormatHint:](./assetwriterinputwithmediatype_outputsettings_sourceformathint_.md)
  Returns a new input that appends sample buffers of the specified type and format hint to the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:sourceformathint:))*