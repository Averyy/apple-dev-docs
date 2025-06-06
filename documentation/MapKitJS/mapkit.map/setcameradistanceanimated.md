# setCameraDistanceAnimated

**Framework**: MapKit JS  
**Kind**: method

Changes the map’s camera distance with an animated transition.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
mapkit.Map setCameraDistanceAnimated(
	number distance,
	optional boolean animate
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns the containing map instance object.

#### Discussion

By default, the change of distance animates.

## Parameters

- `distance`: The altitude of the camera from the center of the map. It’s value needs to be greater than or equal to  .
- `animate`: A Boolean value that determines whether MapKit JS animates the visible area change. The default value is  .

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
- [cameraBoundary](mapkit.map/cameraboundary.md)
  A constraint of the location of the center of the map.
- [setCameraBoundaryAnimated](mapkit.map/setcameraboundaryanimated.md)
  Changes the map’s camera boundary with an animated transition.
- [cameraDistance](mapkit.map/cameradistance.md)
  The altitude of the camera relative to the elevation of the center of the map.
- [cameraZoomRange](mapkit.map/camerazoomrange.md)
  The minimum and maximum distances of the camera from the map center.
- [setCameraZoomRangeAnimated](mapkit.map/setcamerazoomrangeanimated.md)
  Changes the map’s camera zoom range with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/setcameradistanceanimated)*