# ARGeoTrackingStatus.Accuracy.low

**Framework**: ARKit  
**Kind**: case

Geo-tracking accuracy is low.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case low
```

#### Discussion

This value indicates that visual localization is complete and geo-tracking accuracy is low.

One technique an app can use to deal with low accuracy is to render location anchors with an asset that’s more forgiving, like a large ball. If an app renders the ball further in the air, any offset that results from low accuracy will be less noticeable, and less critical to the user.

## See Also

- [ARGeoTrackingStatus.Accuracy.high](argeotrackingstatus/accuracy-swift.enum/high.md)
  Geo-tracking accuracy is high.
- [ARGeoTrackingStatus.Accuracy.undetermined](argeotrackingstatus/accuracy-swift.enum/undetermined.md)
  Geo-tracking accuracy is undetermined.
- [ARGeoTrackingStatus.Accuracy.medium](argeotrackingstatus/accuracy-swift.enum/medium.md)
  Geo-tracking accuracy is average.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/accuracy-swift.enum/low)*