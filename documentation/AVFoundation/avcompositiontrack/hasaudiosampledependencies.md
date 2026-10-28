# hasAudioSampleDependencies

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track has sample dependencies.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var hasAudioSampleDependencies: Bool { get }
```

## Discussion

The value is always [`false`](../../Swift/false.md) for nonaudible media.

## See Also

### Accessing audible characteristics
- [var preferredVolume: Float](./preferredvolume.md)
  The track’s volume preference for playing its audible media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/hasaudiosampledependencies)*