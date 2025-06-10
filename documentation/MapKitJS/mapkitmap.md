# mapkit.Map

**Framework**: MapKit JS  
**Kind**: class

An embeddable interactive map that you add to a webpage.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Map
```

## Mentions

- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Overview

A map is a self-contained view object that you embed on a webpage. It’s possible to have multiple independent maps on a single webpage, although typically webpages only need one interactive map.

## Topics

### Creating a map
- [mapkit.Map](mapkit.map/mapkit.map.md)
  Creates a map you embed on a webpage and initializes it with the constructor options you choose.
- [MapConstructorOptions](mapconstructoroptions.md)
  An object that contains options for creating a map’s features.
### Handling map events
- [Handling map events](handling-map-events.md)
  Register an event lister for events that a map object dispatches.
- [addEventListener](mapkit.map/addeventlistener.md)
  Adds an event listener to handle events that user interactions and the framework trigger.
- [removeEventListener](mapkit.map/removeeventlistener.md)
  Removes an event listener.
### Accessing interaction properties
- [isRotationAvailable](mapkit.map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isRotationEnabled](mapkit.map/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isScrollEnabled](mapkit.map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](mapkit.map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.
### Manipulating the visible portion of the map
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
### Showing the map’s controls
- [showsCompass](mapkit.map/showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [showsMapTypeControl](mapkit.map/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsScale](mapkit.map/showsscale.md)
  A feature visibility setting that determines when the map displays the map’s scale indicator.
- [showsUserLocationControl](mapkit.map/showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](mapkit.map/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.
### Configuring the map’s appearance
- [colorScheme](mapkit.map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [mapkit.Map.ColorSchemes](mapkit.map.colorschemes.md)
  Constants indicating the color scheme of the map.
- [distances](mapkit.map/distances.md)
  The system of measurement that displays on the map.
- [mapkit.Map.Distances](mapkit.map.distances.md)
  Constants indicating the system of measurement that displays on the map.
- [mapType](mapkit.map/maptype.md)
  The type of data that the map displays.
- [mapkit.Map.MapTypes](mapkit.map.maptypes.md)
  Constants representing the type of map to display.
- [padding](mapkit.map/padding.md)
  The map’s inset margins.
- [pointOfInterestFilter](mapkit.map/pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
- [showsPointsOfInterest](mapkit.map/showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [showItems](mapkit.map/showitems.md)
  Adjusts the map’s visible region to bring the specified overlays and annotations into view.
- [MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](mapkit.map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.
### Annotating the map
- [annotations](mapkit.map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](mapkit.map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](mapkit.map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect](mapkit.map/annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation](mapkit.map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations](mapkit.map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation](mapkit.map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations](mapkit.map/removeannotations.md)
  Removes multiple annotations from the map.
### Adding and removing overlays
- [overlays](mapkit.map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](mapkit.map/selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint](mapkit.map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay](mapkit.map/addoverlay.md)
  Adds an overlay to the map.
- [addOverlays](mapkit.map/addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay](mapkit.map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays](mapkit.map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint](mapkit.map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.
### Adding and removing geographical features
- [addItems](mapkit.map/additems.md)
  Adds a collection of annotations, overlays, or other item collections to the map.
- [removeItems](mapkit.map/removeitems.md)
  Removes a collection of annotations, overlays, or other item collections from the map.
### Adding and removing tile overlays
- [tileOverlays](mapkit.map/tileoverlays.md)
  An array of all of the map’s tile overlays.
- [addTileOverlay](mapkit.map/addtileoverlay.md)
  Adds a tile overlay to the map.
- [addTileOverlays](mapkit.map/addtileoverlays.md)
  Adds an array of tile overlays to the map.
- [removeTileOverlay](mapkit.map/removetileoverlay.md)
  Removes a tile overlay from the map.
- [removeTileOverlays](mapkit.map/removetileoverlays.md)
  Removes an array of tile overlays from the map.
### Exploring at street level
- [mapkit.LookAround](mapkit.lookaround.md)
  A view that allows someone to see a street level view of a place.
- [LookAroundOptions](lookaroundoptions.md)
  Options for initializing a LookAround view.
- [mapkit.LookAroundPreview](mapkit.lookaroundpreview.md)
  A class that renders a preview of a LookAround view.
- [LookAroundPreviewOptions](lookaroundpreviewoptions.md)
  Options for initializing a LookAroundPreview object.
- [mapkit.LookAroundScene](mapkit.lookaroundscene.md)
  Object that represents the current location of the view.
- [CommonLookAroundOptions](commonlookaroundoptions.md)
  Options that control the behavior of Look Around views.
### Displaying the user’s location
- [showsUserLocation](mapkit.map/showsuserlocation.md)
  A Boolean value that determines whether to show the user’s location on the map.
- [tracksUserLocation](mapkit.map/tracksuserlocation.md)
  A Boolean value that determines whether to center the map on the user’s location.
- [userLocationAnnotation](mapkit.map/userlocationannotation.md)
  An annotation that indicates the user’s location on the map.
### Converting map coordinates
- [convertCoordinateToPointOnPage](mapkit.map/convertcoordinatetopointonpage.md)
  Converts a coordinate on the map to a point in the page’s coordinate system.
- [convertPointOnPageToCoordinate](mapkit.map/convertpointonpagetocoordinate.md)
  Converts a point in page coordinates to the corresponding map coordinate.
### Destroying a map
- [destroy](mapkit.map/destroy.md)
  Removes the map’s element from the DOM and releases internal references to the map to free up memory.
### Accessing the element
- [element](mapkit.map/element.md)
  The map’s DOM element.
### Selecting map features
- [selectableMapFeatures](mapkit.map/selectablemapfeatures.md)
  An array of map features that users can select from the map.
- [selectableMapFeatureSelectionAccessory](mapkit.map/selectablemapfeatureselectionaccessory.md)
  An accessory for displaying place information when a person selects a map feature.
- [annotationForMapFeature](mapkit.map/annotationformapfeature.md)
  The method MapKit JS calls when the framework creates a map feature annotation.
### Prioritizing feature loading
- [loadPriority](mapkit.map/loadpriority.md)
  A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.
- [mapkit.Map.LoadPriorities](mapkit.map.loadpriorities.md)
  Values for prioritizing the visibility of specific map features while the map is loading.

## See Also

- [maps](mapkit/maps.md)
  An array that automatically adds and removes maps as the framework creates and destroys them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map)*