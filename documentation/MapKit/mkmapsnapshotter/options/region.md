# region

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The area of the map that you want to capture.

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
var region: MKCoordinateRegion { get set }
```

```objc
@property (nonatomic, assign) MKCoordinateRegion region;
```

## Discussion

Use this property to specify the map using geographical coordinates. If you assign a value for this property, the snapshotter updates the value in the [`mapRect`](./maprect.md) property to match the corresponding area as closely as possible.

The snapshotter sets the default value of this property to an area that encompasses the user’s country or region, based on the current locale information.

## See Also

### Configuring the snapshot region
- [var mapRect: MKMapRect](./maprect.md)
  The map rectangle that you want to capture.
- [var camera: MKMapCamera](./camera.md)
  The camera to use when taking the map snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/region)*