# region

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The area the map is displaying.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get region(): CoordinateRegion;
set region(region: CoordinateRegionData);
```

## Mentions

- [Migrating from Version 5 to Version 6](../migrating-from-version-5-to-version-6.md)

## Discussion

This is the area currently displayed by the map, defined with a [`CoordinateRegion`](../coordinateregion.md):

```javascript
const center = new mapkit.Coordinate(48.8468, 2.3364),
    span = new mapkit.CoordinateSpan(0.016, 0.016),
    region = new mapkit.CoordinateRegion(center, span);
```

## See Also

### Manipulating the visible portion of the map
- [center](./center.md)
  The map coordinate at the center of the map view.
- [setCenterAnimated(coordinate, animated)](./setcenteranimated.md)
  Centers the map to the provided coordinate, with optional animation.
- [setRegionAnimated(region, animated)](./setregionanimated.md)
  Changes the map’s region to the provided region, with optional animation.
- [rotation](./rotation.md)
  The map’s rotation, in degrees.
- [setRotationAnimated(degrees, animated)](./setrotationanimated.md)
  Changes the map’s rotation setting to the number of specified degrees.
- [visibleMapRect](./visiblemaprect.md)
  The visible area of the map, in map units.
- [setVisibleMapRectAnimated(mapRect, animated)](./setvisiblemaprectanimated.md)
  Changes the map’s visible map rectangle to the specified map rectangle.
- [cameraBoundary](./cameraboundary.md)
  A constraint of the location of the center of the map.
- [setCameraBoundaryAnimated(cameraBoundary, animated)](./setcameraboundaryanimated.md)
  Changes the map’s camera boundary with an animated transition.
- [interface CameraBoundaryDescription](../cameraboundarydescription.md)
  An object literal that contains information defining an area on the map.
- [cameraDistance](./cameradistance.md)
  The altitude of the camera relative to the elevation of the center of the map.
- [setCameraDistanceAnimated(distance, animated)](./setcameradistanceanimated.md)
  Changes the map’s camera distance with an animated transition.
- [cameraZoomRange](./camerazoomrange.md)
  The minimum and maximum distances of the camera from the map center.
- [setCameraZoomRangeAnimated(cameraZoomRange, animated)](./setcamerazoomrangeanimated.md)
  Changes the map’s camera zoom range with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/region)*