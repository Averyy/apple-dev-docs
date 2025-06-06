# mapRect

**Framework**: MapKit  
**Kind**: property

The map rectangle that you want to capture.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var mapRect: MKMapRect { get set }
```

#### Discussion

Use this property to specify the map using map view points. If you assign a value for this property, the snapshotter updates the value in the [`region`](mkmapsnapshotter/options/region.md) property to match the corresponding map rectangle as closely as possible.

The snapshotter sets the default value of this property to a map rectangle that encompasses the user’s country or region, based on the current locale information.

## See Also

- [var region: MKCoordinateRegion](mkmapsnapshotter/options/region.md)
  The area of the map that you want to capture.
- [var camera: MKMapCamera](mkmapsnapshotter/options/camera.md)
  The camera to use when taking the map snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/maprect)*