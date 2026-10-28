# hasAudioSampleDependencies

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the track has sample dependencies.

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
static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

The value is always [`false`](../../Swift/false.md) for nonaudible media.

## See Also

### Loading audible characteristics
- [static var preferredVolume: AVAsyncProperty<Root, Float>](./preferredvolume-8q2yt.md)
  The track’s volume preference for playing its audible media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/hasaudiosampledependencies)*