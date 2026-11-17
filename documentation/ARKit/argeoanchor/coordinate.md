# coordinate

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The latitude and longitude of the anchor’s geographic location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var coordinate: CLLocationCoordinate2D { get }
```

```objc
@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
```

## Discussion

This property is set by the app at anchor initialization. The anchor’s transform will be automatically updated by the session when `ARGeoTrackingConfiguration` is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/coordinate)*