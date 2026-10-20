# setCamera(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func setCamera(_ camera: MKMapCamera, animated: Bool)
```

```objc
- (void) setCamera:(MKMapCamera *) camera animated:(BOOL) animated;
```

## Parameters

- `camera`: The camera object containing the viewing angle information. This parameter can’t be `nil`.
- `animated`: Specify [`true`](../../Swift/true.md) if you want the map view to animate the change in viewing angle, or [`false`](../../Swift/false.md) if you want the map to reflect the changes without animations.

## See Also

### Configuring the map display
- [var camera: MKMapCamera](./camera.md)
  The camera to use for determining the appearance of the map.
- [var showsCompass: Bool](./showscompass.md)
  A Boolean value that indicates whether the map displays a compass control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setcamera(_:animated:))*