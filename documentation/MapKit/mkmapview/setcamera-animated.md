# setCamera(_:animated:)

**Framework**: MapKit  
**Kind**: method

Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCamera(_ camera: MKMapCamera, animated: Bool)
```

## Parameters

- `camera`: The camera object containing the viewing angle information. This parameter can’t be  .
- `animated`: Specify   if you want the map view to animate the change in viewing angle, or   if you want the map to reflect the changes without animations.

## See Also

- [var camera: MKMapCamera](mkmapview/camera.md)
  The camera to use for determining the appearance of the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setcamera(_:animated:))*