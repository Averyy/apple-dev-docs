# setRegionAnimated(region, animated)

**Framework**: MapKit JS  
**Kind**: method

Changes the map’s region to the provided region, with optional animation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
setRegionAnimated(region: CoordinateRegion, animated?: boolean): Map;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns the map object.

#### Discussion

By default, MapKit JS animates the change.

## Parameters

- `region`: A new   for the map to display.
- `animate`: A Boolean value that determines whether MapKit JS animates the region change. The default value is  .

## See Also

- [center](map/center.md)
  The map coordinate at the center of the map view.
- [setCenterAnimated(coordinate, animated)](map/setcenteranimated.md)
  Centers the map to the provided coordinate, with optional animation.
- [region](map/region.md)
  The area the map is displaying.
- [rotation](map/rotation.md)
  The map’s rotation, in degrees.
- [setRotationAnimated(degrees, animated)](map/setrotationanimated.md)
  Changes the map’s rotation setting to the number of specified degrees.
- [visibleMapRect](map/visiblemaprect.md)
  The visible area of the map, in map units.
- [setVisibleMapRectAnimated(mapRect, animated)](map/setvisiblemaprectanimated.md)
  Changes the map’s visible map rectangle to the specified map rectangle.
- [cameraBoundary](map/cameraboundary.md)
  A constraint of the location of the center of the map.
- [setCameraBoundaryAnimated(mapRect, animated)](map/setcameraboundaryanimated.md)
  Changes the map’s camera boundary with an animated transition.
- [interface CameraBoundaryDescription](cameraboundarydescription.md)
  An object literal that contains information defining an area on the map.
- [cameraDistance](map/cameradistance.md)
  The altitude of the camera relative to the elevation of the center of the map.
- [setCameraDistanceAnimated(distance, animated)](map/setcameradistanceanimated.md)
  Changes the map’s camera distance with an animated transition.
- [cameraZoomRange](map/camerazoomrange.md)
  The minimum and maximum distances of the camera from the map center.
- [setCameraZoomRangeAnimated(cameraZoomRange, animated)](map/setcamerazoomrangeanimated.md)
  Changes the map’s camera zoom range with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/setregionanimated)*