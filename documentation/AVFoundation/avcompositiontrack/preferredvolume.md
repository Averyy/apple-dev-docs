# preferredVolume

**Framework**: AVFoundation  
**Kind**: property

The track’s volume preference for playing its audible media.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var preferredVolume: Float { get }
```

#### Discussion

The preferred volume for an audio track is typically, but not always, `1.0`. For non-audible tracks, the value is `0.0`.

## See Also

- [var hasAudioSampleDependencies: Bool](avcompositiontrack/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/preferredvolume)*