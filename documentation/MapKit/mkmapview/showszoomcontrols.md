# showsZoomControls

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map displays zoom controls.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
@MainActor
var showsZoomControls: Bool { get set }
```

#### Discussion

In macOS, use this property to show or hide the controls that let users change the zoom level of the map.

## See Also

- [func setCamera(MKMapCamera, animated: Bool)](mkmapview/setcamera(_:animated:).md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [var camera: MKMapCamera](mkmapview/camera.md)
  The camera to use for determining the appearance of the map.
- [var showsCompass: Bool](mkmapview/showscompass.md)
  A Boolean value that indicates whether the map displays a compass control.
- [var showsPitchControl: Bool](mkmapview/showspitchcontrol.md)
  A Boolean value that indicates whether the map displays the pitch control.
- [var showsScale: Bool](mkmapview/showsscale.md)
  A Boolean value that indicates whether the map shows scale information.
- [var showsBuildings: Bool](mkmapview/showsbuildings.md)
  A Boolean value that indicates whether the map displays extruded building information on supported map types.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapview/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](mkmapview/showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showszoomcontrols)*