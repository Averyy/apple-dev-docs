# sourceReadySampleBuffer(byTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns the source CMReadySampleBuffer for the given track ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func sourceReadySampleBuffer(byTrackID trackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?
```

#### Return Value

The source CMReadySampleBuffer for the given track ID.

## Parameters

- `trackID`: The track ID for the requested source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcereadysamplebuffer(bytrackid:))*