# makeResumableWriterInput(for:outputSettings:sourceFormatHint:)

**Framework**: AVFoundation  
**Kind**: method

Helper function that returns a minimally configured AVAssetWriterInput object for writing the current segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeResumableWriterInput(for mediaType: AVMediaType, outputSettings: [String : any Sendable]? = nil, sourceFormatHint: CMFormatDescription? = nil) throws -> AVAssetWriterInput
```

#### Return Value

A new writer input.

#### Discussion

The final video encoder state from the previous segment will be restored before writing starts.

Clients using AVAssetWriterInput with video compression must use this method to create the writer input for writing the segment. The planner initializes the writer input in such a way that when writing starts, the video encoder’s state is restored to the final state of the last segment. The client should perform additional configurations on the returned writer input as needed, but must apply the same configurations for each segment of the track.

Client cannot call this method more than once on a writing request object. For the same segment writing request, this method and the “createResumableCompressionSessionWithAllocator” method are mutually exclusive. The client can call either one of the two, but not both. This method fails (returns nil) with error if the outputSettings or sourceFormatHint differs from the previous segment.

The writing request retains the writer input but does not mutate it after this method is returned.

> **Note**: An error if the input cannot be created or if settings differ from previous segment.

## Parameters

- `mediaType`: The type of media that an input accepts.
- `outputSettings`: The settings to use for configuring the AVAssetWriterInput object to be returned. Create an output settings dictionary manually, or use AVOutputSettingsAssistant to create preset-based settings.
- `sourceFormatHint`: A hint about the format of the media data to append. The input uses the source format hint to fill in missing output settings. If you specify a hint, you only need to specify AVFormatIDKey for the audio output settings, and AVVideoCodecKey is the only required key for video output settings. The system raises an error if the format description isn’t valid for the indicated media type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest/makeresumablewriterinput(for:outputsettings:sourceformathint:))*