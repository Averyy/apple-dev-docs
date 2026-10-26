# preferredVolume

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The track’s volume preference for playing its audible media.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`preferredVolume`](../avpartialasyncproperty/preferredvolume-8q2yt.md) asynchronously instead.

## Declaration

```swift
var preferredVolume: Float { get }
```

```objc
@property (nonatomic, readonly) float preferredVolume;
```

#### Discussion

The preferred volume for an audio track is typically, but not always, `1.0`. For non-audible tracks, the value is `0.0`.

## See Also

### Accessing audible characteristics
- [hasAudioSampleDependencies](./hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/preferredvolume)*