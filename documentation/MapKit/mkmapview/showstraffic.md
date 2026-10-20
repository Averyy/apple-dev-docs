# showsTraffic

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map displays traffic information.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2
- iPadOS 9.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.11+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MKStandardMapConfiguration`](../mkstandardmapconfiguration.md) or [`MKHybridMapConfiguration`](../mkhybridmapconfiguration.md) and configure the `showsTraffic` property instead.

## Declaration

```swift
var showsTraffic: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsTraffic;
```

#### Discussion

The [`mapType`](./maptype.md) property must be set to [`MKMapType.standard`](../mkmaptype/standard.md) or [`MKMapType.hybrid`](../mkmaptype/hybrid.md) for traffic information to be shown. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the map display
- [func setCamera(MKMapCamera, animated: Bool)](./setcamera%28_,animated%29.md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showstraffic)*