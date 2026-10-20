# naturalTimeScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The natural time scale of the media that a track references.

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
static var naturalTimeScale: AVAsyncProperty<Root, CMTimeScale> { get }
```

Available when `Root` inherits `AVAssetTrack`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading temporal information
- [static var timeRange: AVAsyncProperty<Root, CMTimeRange>](./timerange.md)
  The time range of the track within the overall timeline of the asset.
- [static var estimatedDataRate: AVAsyncProperty<Root, Float>](./estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/naturaltimescale)*