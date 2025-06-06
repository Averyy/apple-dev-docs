# camera

**Framework**: MapKit  
**Kind**: property

The camera to use for determining the appearance of the map.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var camera: MKMapCamera { get set }
```

#### Discussion

A camera object defines a point above the map’s surface from which to view the map. Applying a camera to a map can have the effect of giving the map a 3D-like appearance. You can use a camera to rotate the map so that it orients to match the user’s heading or to apply a pitch angle to tilt the plane of the map. You can check the map’s [`isPitchEnabled`](mkmapview/ispitchenabled.md) property to determine whether the map can use pitch.

Assigning a new camera to this property updates the map immediately and without animating the change. If you want to animate changes in camera position, use the [`setCamera(_:animated:)`](mkmapview/setcamera(_:animated:).md) method instead.

Don’t set this property to `nil`. To restore the map to a flat appearance, apply a camera with a pitch angle of `0`, which yields a camera looking straight down onto the map surface.

## See Also

- [func setCamera(MKMapCamera, animated: Bool)](mkmapview/setcamera(_:animated:).md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [var showsCompass: Bool](mkmapview/showscompass.md)
  A Boolean value that indicates whether the map displays a compass control.
- [var showsPitchControl: Bool](mkmapview/showspitchcontrol.md)
  A Boolean value that indicates whether the map displays the pitch control.
- [var showsScale: Bool](mkmapview/showsscale.md)
  A Boolean value that indicates whether the map shows scale information.
- [var showsZoomControls: Bool](mkmapview/showszoomcontrols.md)
  A Boolean value that indicates whether the map displays zoom controls.
- [var showsBuildings: Bool](mkmapview/showsbuildings.md)
  A Boolean value that indicates whether the map displays extruded building information on supported map types.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapview/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](mkmapview/showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camera)*