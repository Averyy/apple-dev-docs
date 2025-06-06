# naturalTimeScale

**Framework**: AVFoundation  
**Kind**: property

The natural time scale of the media that a track references.

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
static var naturalTimeScale: AVAsyncProperty<Root, CMTimeScale> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [static var timeRange: AVAsyncProperty<Root, CMTimeRange>](avpartialasyncproperty/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [static var estimatedDataRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/naturaltimescale)*