# sourceReadOnlyPixelBuffer(byTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func sourceReadOnlyPixelBuffer(byTrackID trackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?
```

#### Return Value

The source CVReadOnlyPixelBuffer for the given track ID.

## Parameters

- `trackID`: The track ID for the requested source frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer(bytrackid:))*