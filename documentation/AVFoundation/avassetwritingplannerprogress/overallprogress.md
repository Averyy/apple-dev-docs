# overallProgress

**Framework**: AVFoundation  
**Kind**: property

The overall progress across all tracks.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var overallProgress: Float { get }
```

#### Discussion

Returns a float value between 0.0 and 1.0 representing the overall progress. This is calculated as the average progress of all tracks weighted by their durations.

## See Also

- [func progress(forTrack: CMPersistentTrackID) -> Float](avassetwritingplannerprogress/progress(fortrack:).md)
  Returns the progress for a specific track identified by its assemblyTrackID.
- [func progress(forTrack: CMPersistentTrackID) -> Float](avassetwritingplannerprogress/progress(fortrack:).md)
  Returns the progress for a specific track identified by its assemblyTrackID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress/overallprogress)*