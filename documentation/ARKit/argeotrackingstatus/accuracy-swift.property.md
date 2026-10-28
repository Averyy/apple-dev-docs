# accuracy

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The accuracy of geo tracking at the time the session captured the frame.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var accuracy: ARGeoTrackingStatus.Accuracy { get }
```

```objc
@property (nonatomic, readonly) ARGeoTrackingAccuracy accuracy;
```

## Discussion

ARKit populates this property after reaching [`ARGeoTrackingStatus.State.localized`](./state-swift.enum/localized.md). To ensure the best possible user experience, an app must monitor and react to the geo-tracking accuracy. For more information, see [`ARGeoTrackingStatus.Accuracy`](./accuracy-swift.enum.md).

## See Also

### Judging Accuracy
- [ARGeoTrackingStatus.Accuracy](./accuracy-swift.enum.md)
  Values that are possible for the current accuracy of geo tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/accuracy-swift.property)*