# ARGeoTrackingStatus.Accuracy.low

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

Geo-tracking accuracy is low.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
case low
```

```c
ARGeoTrackingAccuracyLow
```

#### Discussion

This value indicates that visual localization is complete and geo-tracking accuracy is low.

One technique an app can use to deal with low accuracy is to render location anchors with an asset that’s more forgiving, like a large ball. If an app renders the ball further in the air, any offset that results from low accuracy will be less noticeable, and less critical to the user.

## See Also

### Accuracies
- [ARGeoTrackingStatus.Accuracy.high](./high.md)
  Geo-tracking accuracy is high.
- [ARGeoTrackingStatus.Accuracy.undetermined](./undetermined.md)
  Geo-tracking accuracy is undetermined.
- [ARGeoTrackingStatus.Accuracy.medium](./medium.md)
  Geo-tracking accuracy is average.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/accuracy-swift.enum/low)*