# preferredVolume

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The track’s volume preference for playing its audible media.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredVolume: AVAsyncProperty<Root, Float> { get }
```

Available when `Root` inherits `AVAssetTrack`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

The preferred volume for an audio track is typically, but not always, `1.0`. For nonaudible tracks, the value is `0.0`.

## See Also

### Loading audible characteristics
- [static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool>](./hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredvolume-8q2yt)*