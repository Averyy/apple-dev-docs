# showsBuildings

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map displays extruded building information on supported map types.

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
var showsBuildings: Bool { get set }
```

#### Discussion

> **Note**:  In iOS 16 and macOS 13, and later, when overlay content is present, this property has no effect and the map renders buildings and trees as transparent. This enables content to be clearly visible while preserving the context of the surroundings.

When this property is [`true`](https://developer.apple.com/documentation/swift/true) and the camera has a pitch angle greater than zero, the map extrudes buildings so that they extend above the map plane, creating a 3D effect. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

To display extruded buildings, set the [`mapType`](mkmapview/maptype.md) property to [`MKMapType.standard`](mkmaptype/standard.md) or [`MKMapType.mutedStandard`](mkmaptype/mutedstandard.md).

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
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapview/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](mkmapview/showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showsbuildings)*