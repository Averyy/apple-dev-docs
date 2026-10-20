# setCameraDistanceAnimated(distance, animated)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Changes the map’s camera distance with an animated transition.

**Availability**:
- MapKit JS 5.23+

## Declaration

```
setCameraDistanceAnimated(distance: number, animated?: boolean): Map;
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Return Value

Returns the containing map instance object.

#### Discussion

By default, the change of distance animates.

## Parameters

- `distance`: The altitude of the camera from the center of the map. It’s value needs to be greater than or equal to `0`.
- `animate`: A Boolean value that determines whether MapKit JS animates the visible area change. The default value is `true`.

## See Also

### Manipulating the visible portion of the map
- [center](./center.md)
  The map coordinate at the center of the map view.
- [setCenterAnimated(coordinate, animated)](./setcenteranimated.md)
  Centers the map to the provided coordinate, with optional animation.
- [region](./region.md)
  The area the map is displaying.
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
- [cameraZoomRange](./camerazoomrange.md)
  The minimum and maximum distances of the camera from the map center.
- [setCameraZoomRangeAnimated(cameraZoomRange, animated)](./setcamerazoomrangeanimated.md)
  Changes the map’s camera zoom range with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/setcameradistanceanimated)*