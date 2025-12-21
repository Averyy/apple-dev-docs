# hasAudioSampleDependencies

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track has sample dependencies.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

The value is always [`false`](https://developer.apple.com/documentation/Swift/false) for nonaudible media.

## See Also

- [static var preferredVolume: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredvolume-8q2yt.md)
  The track’s volume preference for playing its audible media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/hasaudiosampledependencies)*