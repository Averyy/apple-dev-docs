# showsBuildings

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map displays extruded building information on supported map types.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MKStandardMapConfiguration`](../mkstandardmapconfiguration.md) instead.

## Declaration

```swift
var showsBuildings: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsBuildings;
```

#### Discussion

> **Note**:  In iOS 16 and macOS 13, and later, when overlay content is present, this property has no effect and the map renders buildings and trees as transparent. This enables content to be clearly visible while preserving the context of the surroundings.

When this property is [`true`](../../Swift/true.md) and the camera has a pitch angle greater than zero, the map extrudes buildings so that they extend above the map plane, creating a 3D effect. The default value of this property is [`true`](../../Swift/true.md).

To display extruded buildings, set the [`mapType`](./maptype.md) property to [`MKMapType.standard`](../mkmaptype/standard.md) or [`MKMapType.mutedStandard`](../mkmaptype/mutedstandard.md).

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
- [var showsPointsOfInterest: Bool](./showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](./showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showsbuildings)*