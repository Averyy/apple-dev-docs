# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The time range of the track within the overall timeline of the asset.

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
static var timeRange: AVAsyncProperty<Root, CMTimeRange> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

If the start of the time range is greater than [`zero`](../../CoreMedia/cmtime/zero.md), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

## See Also

### Loading temporal information
- [static var naturalTimeScale: AVAsyncProperty<Root, CMTimeScale>](./naturaltimescale.md)
  The natural time scale of the media that a track references.
- [static var estimatedDataRate: AVAsyncProperty<Root, Float>](./estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/timerange)*