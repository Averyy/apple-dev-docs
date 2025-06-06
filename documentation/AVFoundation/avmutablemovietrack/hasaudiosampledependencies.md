# hasAudioSampleDependencies

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track has sample dependencies.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var hasAudioSampleDependencies: Bool { get }
```

#### Discussion

The value is always [`false`](https://developer.apple.com/documentation/swift/false) for nonaudible media.

## See Also

- [var preferredVolume: Float](avmutablemovietrack/preferredvolume.md)
  The preferred volume for the audible medata data of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/hasaudiosampledependencies)*