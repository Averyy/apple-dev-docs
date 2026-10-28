# showsCompass

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map displays a compass control.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
var showsCompass: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsCompass;
```

## Discussion

Use this property to show or hide a control that lets users change the heading orientation of the map.

## See Also

### Configuring the map display
- [func setCamera(MKMapCamera, animated: Bool)](./setcamera%28_,animated%29.md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [var camera: MKMapCamera](./camera.md)
  The camera to use for determining the appearance of the map.
- [var showsPitchControl: Bool](./showspitchcontrol.md)
  A Boolean value that indicates whether the map displays the pitch control.
- [var showsScale: Bool](./showsscale.md)
  A Boolean value that indicates whether the map shows scale information.
- [var showsZoomControls: Bool](./showszoomcontrols.md)
  A Boolean value that indicates whether the map displays zoom controls.
- [var showsBuildings: Bool](./showsbuildings.md)
  A Boolean value that indicates whether the map displays extruded building information on supported map types.
- [var showsPointsOfInterest: Bool](./showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](./showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showscompass)*