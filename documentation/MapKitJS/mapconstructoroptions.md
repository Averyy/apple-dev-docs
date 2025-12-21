# MapConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

An object that contains options for creating a map’s features.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface MapConstructorOptions
```

#### Overview

Use [`MapConstructorOptions`](mapconstructoroptions.md) to set the initial characteristics for your map, including the visible portion of the map, which controls are visible, the configuration of overlays and annotations, and the visibility of the user’s location.

## Topics

### Controlling the visible portion of the map
- [visibleMapRect](mapconstructoroptions/visiblemaprect.md)
  The visible area of the map, in map units.
- [region](mapconstructoroptions/region.md)
  The area the map is displaying.
- [center](mapconstructoroptions/center.md)
  The map coordinate at the center of the map view.
- [rotation](mapconstructoroptions/rotation.md)
  The map’s rotation, in degrees.
- [tintColor](mapconstructoroptions/tintcolor.md)
  The CSS color that MapKit JS uses for the user interface controls on the map.
### Setting the map’s appearance and controls
- [colorScheme](mapconstructoroptions/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [mapType](mapconstructoroptions/maptype.md)
  The type of data that the map view displays.
- [padding](mapconstructoroptions/padding.md)
  The map’s inset margins.
- [showsMapTypeControl](mapconstructoroptions/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [isRotationEnabled](mapconstructoroptions/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [showsCompass](mapconstructoroptions/showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [isZoomEnabled](mapconstructoroptions/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.
- [showsZoomControl](mapconstructoroptions/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.
- [isScrollEnabled](mapconstructoroptions/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll the map with a pointing device or gestures on a touchscreen.
- [showsScale](mapconstructoroptions/showsscale.md)
  A feature visibility setting that allows you to determine when to display the map’s scale.
### Configuring map annotations
- [annotationForCluster](mapconstructoroptions/annotationforcluster.md)
  Modifies cluster annotations.
- [annotations](mapconstructoroptions/annotations.md)
  An array holding all the annotations on the map.
- [selectedAnnotation](mapconstructoroptions/selectedannotation.md)
  The selected annotation on the map.
### Configuring map overlays
- [overlays](mapconstructoroptions/overlays.md)
  An array that contains all of the map’s overlays.
- [selectedOverlay](mapconstructoroptions/selectedoverlay.md)
  The selected overlay on the map.
- [showsPointsOfInterest](mapconstructoroptions/showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [pointOfInterestFilter](mapconstructoroptions/pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
### Enabling user location
- [showsUserLocation](mapconstructoroptions/showsuserlocation.md)
  A Boolean value that determines whether to show the user’s location on the map.
- [tracksUserLocation](mapconstructoroptions/tracksuserlocation.md)
  A Boolean value that determines whether to center the map on the user’s location.
- [showsUserLocationControl](mapconstructoroptions/showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
### Setting the loading priority
- [loadPriority](mapconstructoroptions/loadpriority.md)
  A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.
- [const LoadPriority](loadpriority.md)
  Values for prioritizing the visibility of specific map features while the map is loading.
### Instance Properties
- [annotationForMapFeature](mapconstructoroptions/annotationformapfeature.md)
  The method MapKit JS calls when the framework creates a map feature annotation.
- [cameraBoundary](mapconstructoroptions/cameraboundary.md)
  The boundary of the area within which the map view’s center needs to remain.
- [cameraDistance](mapconstructoroptions/cameradistance.md)
  The altitude of the camera relative to the elevation of the center of the map.
- [cameraZoomRange](mapconstructoroptions/camerazoomrange.md)
  Values that set the minimum and maximum distances of the camera from the map center.
- [distances](mapconstructoroptions/distances.md)
  The system of measurement that displays on the map.
- [selectableMapFeatures](mapconstructoroptions/selectablemapfeatures.md)
  An array of map features that someone can select from the map.
- [tileOverlays](mapconstructoroptions/tileoverlays.md)
  An array of the map tile overlays.

## See Also

- [new Map(parent, options)](map/mapconstructor.md)
  Creates a map you embed on a webpage and initializes it with the constructor options you choose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions)*