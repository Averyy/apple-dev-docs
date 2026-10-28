# ARGeoTrackingStatus.Accuracy

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Values that are possible for the current accuracy of geo tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum Accuracy
```

```c
enum ARGeoTrackingAccuracy : NSInteger;
```

## Discussion

To ensure the best possible user experience, an app must monitor and react to the geo-tracking accuracy. When accuracy is [`ARGeoTrackingStatus.Accuracy.low`](./accuracy-swift.enum/low.md), the app needs to show content that’s more forgiving if ARKit is off by a small distance. For example, if accuracy is [`ARGeoTrackingStatus.Accuracy.low`](./accuracy-swift.enum/low.md), rendering a location anchor as a large ball several meters in the air is more appropriate than rendering an arrow that rests its point on a real-world surface. Because a larger ball isn’t meant to mark a precise location, any offset that results from low accuracy will be less noticeable to the user. Apps that need higher-precision location anchors need to wait for [`ARGeoTrackingStatus.Accuracy.medium`](./accuracy-swift.enum/medium.md) or [`ARGeoTrackingStatus.Accuracy.high`](./accuracy-swift.enum/high.md) accuracy before revealing rendered location-anchors, or dismissing user instructions.

## Topics

### Accuracies
- [ARGeoTrackingStatus.Accuracy.high](./accuracy-swift.enum/high.md)
  Geo-tracking accuracy is high.
- [ARGeoTrackingStatus.Accuracy.undetermined](./accuracy-swift.enum/undetermined.md)
  Geo-tracking accuracy is undetermined.
- [ARGeoTrackingStatus.Accuracy.low](./accuracy-swift.enum/low.md)
  Geo-tracking accuracy is low.
- [ARGeoTrackingStatus.Accuracy.medium](./accuracy-swift.enum/medium.md)
  Geo-tracking accuracy is average.
### Initializers
- [init?(rawValue: Int)](./accuracy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Judging Accuracy
- [var accuracy: ARGeoTrackingStatus.Accuracy](./accuracy-swift.property.md)
  The accuracy of geo tracking at the time the session captured the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/accuracy-swift.enum)*