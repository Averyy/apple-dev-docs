# showsTraffic

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map displays traffic information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsTraffic: Bool { get set }
```

#### Discussion

The [`mapType`](mkmapview/maptype.md) property must be set to [`MKMapType.standard`](mkmaptype/standard.md) or [`MKMapType.hybrid`](mkmaptype/hybrid.md) for traffic information to be shown. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

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
- [var showsZoomControls: Bool](mkmapview/showszoomcontrols.md)
  A Boolean value that indicates whether the map displays zoom controls.
- [var showsBuildings: Bool](mkmapview/showsbuildings.md)
  A Boolean value that indicates whether the map displays extruded building information on supported map types.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapview/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showstraffic)*