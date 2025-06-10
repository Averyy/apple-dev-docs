# cameraBoundary

**Framework**: MapKit JS  
**Kind**: property

A constraint of the location of the center of the map.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
attribute CameraBoundaryDescription cameraBoundary;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

An object containing both [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md) and [`mapkit.MapRect`](mapkit.maprect/mapkit.maprect.md) instances.

#### Discussion

Setting this property requires either a [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md) or a [`mapkit.MapRect`](mapkit.maprect.md) instance as a value. Getting the property returns an object containing both [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md) and [`mapkit.MapRect`](mapkit.maprect.md) instances.

## Topics

### Defining a Camera Boundary
- [CameraBoundaryDescription](cameraboundarydescription.md)
  An object literal containing at least one property defining an area on the map.

## See Also

- [center](mapkit.map/center.md)
  The map coordinate at the center of the map view.
- [setCenterAnimated](mapkit.map/setcenteranimated.md)
  Centers the map to the provided coordinate, with optional animation.
- [region](mapkit.map/region.md)
  The area the map is displaying.
- [setRegionAnimated](mapkit.map/setregionanimated.md)
  Changes the map’s region to the provided region, with optional animation.
- [rotation](mapkit.map/rotation.md)
  The map’s rotation, in degrees.
- [setRotationAnimated](mapkit.map/setrotationanimated.md)
  Changes the map’s rotation setting to the number of specified degrees.
- [visibleMapRect](mapkit.map/visiblemaprect.md)
  The visible area of the map, in map units.
- [setVisibleMapRectAnimated](mapkit.map/setvisiblemaprectanimated.md)
  Changes the map’s visible map rectangle to the specified map rectangle.
- [setCameraBoundaryAnimated](mapkit.map/setcameraboundaryanimated.md)
  Changes the map’s camera boundary with an animated transition.
- [CameraBoundaryDescription](cameraboundarydescription.md)
  An object literal containing at least one property defining an area on the map.
- [cameraDistance](mapkit.map/cameradistance.md)
  The altitude of the camera relative to the elevation of the center of the map.
- [setCameraDistanceAnimated](mapkit.map/setcameradistanceanimated.md)
  Changes the map’s camera distance with an animated transition.
- [cameraZoomRange](mapkit.map/camerazoomrange.md)
  The minimum and maximum distances of the camera from the map center.
- [setCameraZoomRangeAnimated](mapkit.map/setcamerazoomrangeanimated.md)
  Changes the map’s camera zoom range with an animated transition.
- [CameraZoomRangeLiteral](camerazoomrangeliteral.md)
  An object literal containing minimum and maximum camera distance in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/cameraboundary)*