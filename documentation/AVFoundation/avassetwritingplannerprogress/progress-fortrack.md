# progress(forTrack:)

**Framework**: AVFoundation  
**Kind**: method

Returns the progress for a specific track identified by its assemblyTrackID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func progress(forTrack assemblyTrackID: CMPersistentTrackID) -> Float
```

#### Return Value

A float value between 0.0 and 1.0 representing the percentage of duration completed for the track. Returns 0.0 if the track ID is not found.

#### Discussion

The progress is calculated as the ratio of completed duration to total duration for the track.

## Parameters

- `assemblyTrackID`: The track ID to query progress for.

## See Also

- [var overallProgress: Float](avassetwritingplannerprogress/overallprogress.md)
  The overall progress across all tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress/progress(fortrack:))*