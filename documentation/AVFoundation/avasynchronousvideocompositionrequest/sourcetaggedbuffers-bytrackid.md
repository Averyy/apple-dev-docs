# sourceTaggedBuffers(byTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns the source tagged buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func sourceTaggedBuffers(byTrackID trackID: CMPersistentTrackID) -> [CMTaggedBuffer]?
```

#### Return Value

The source CMTaggedBuffer array for the given track ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetaggedbuffers(bytrackid:))*