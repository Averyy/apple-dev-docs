# showsPitchControl

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map displays the pitch control.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var showsPitchControl: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsPitchControl;
```

## See Also

### Configuring the map display
- [func setCamera(MKMapCamera, animated: Bool)](./setcamera%28_,animated%29.md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [var camera: MKMapCamera](./camera.md)
  The camera to use for determining the appearance of the map.
- [var showsCompass: Bool](./showscompass.md)
  A Boolean value that indicates whether the map displays a compass control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showspitchcontrol)*