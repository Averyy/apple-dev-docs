# loopDuration

**Framework**: Audio Toolbox  
**Kind**: property

The point in a music track, measured in beats from the end of the music track, at which to begin playback during looped playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var loopDuration: MusicTimeStamp
```

#### Discussion

During looped playback, a music track plays from (`kSequenceTrackProperty_TrackLength` – `loopDuration`) to `kSequenceTrackProperty_TrackLength`.

To explicitly turn off looping, specify a loopDuration of `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musictrackloopinfo/loopduration)*