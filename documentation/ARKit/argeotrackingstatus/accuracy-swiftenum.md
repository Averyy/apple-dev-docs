# ARGeoTrackingStatus.Accuracy

**Framework**: ARKit  
**Kind**: enum

Values that are possible for the current accuracy of geo tracking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Accuracy
```

#### Discussion

To ensure the best possible user experience, an app must monitor and react to the geo-tracking accuracy. When accuracy is [`ARGeoTrackingStatus.Accuracy.low`](argeotrackingstatus/accuracy-swift.enum/low.md), the app needs to show content that’s more forgiving if ARKit is off by a small distance. For example, if accuracy is [`ARGeoTrackingStatus.Accuracy.low`](argeotrackingstatus/accuracy-swift.enum/low.md), rendering a location anchor as a large ball several meters in the air is more appropriate than rendering an arrow that rests its point on a real-world surface. Because a larger ball isn’t meant to mark a precise location, any offset that results from low accuracy will be less noticeable to the user. Apps that need higher-precision location anchors need to wait for [`ARGeoTrackingStatus.Accuracy.medium`](argeotrackingstatus/accuracy-swift.enum/medium.md) or [`ARGeoTrackingStatus.Accuracy.high`](argeotrackingstatus/accuracy-swift.enum/high.md) accuracy before revealing rendered location-anchors, or dismissing user instructions.

## Topics

### Accuracies
- [ARGeoTrackingStatus.Accuracy.high](argeotrackingstatus/accuracy-swift.enum/high.md)
  Geo-tracking accuracy is high.
- [ARGeoTrackingStatus.Accuracy.undetermined](argeotrackingstatus/accuracy-swift.enum/undetermined.md)
  Geo-tracking accuracy is undetermined.
- [ARGeoTrackingStatus.Accuracy.low](argeotrackingstatus/accuracy-swift.enum/low.md)
  Geo-tracking accuracy is low.
- [ARGeoTrackingStatus.Accuracy.medium](argeotrackingstatus/accuracy-swift.enum/medium.md)
  Geo-tracking accuracy is average.
### Initializers
- [init?(rawValue: Int)](argeotrackingstatus/accuracy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var accuracy: ARGeoTrackingStatus.Accuracy](argeotrackingstatus/accuracy-swift.property.md)
  The accuracy of geo tracking at the time the session captured the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/accuracy-swift.enum)*