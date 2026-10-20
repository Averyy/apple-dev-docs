# camera

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The camera to use when taking the map snapshot.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@NSCopying
var camera: MKMapCamera { get set }
```

```objc
@property (nonatomic, copy) MKMapCamera * camera;
```

#### Discussion

Specify a camera object if you want to change the pitch, altitude, or heading information applied to the map.

## See Also

### Configuring the snapshot region
- [var region: MKCoordinateRegion](./region.md)
  The area of the map that you want to capture.
- [var mapRect: MKMapRect](./maprect.md)
  The map rectangle that you want to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/camera)*