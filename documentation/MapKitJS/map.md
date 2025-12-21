# Map

**Framework**: MapKit JS  
**Kind**: class

An embeddable interactive map that you add to a webpage.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Map extends MapKitEventTarget
```

## Mentions

- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Overview

A map is a self-contained view object that you embed on a webpage. It’s possible to have multiple independent maps on a single webpage, although typically webpages only need one interactive map.

## Topics

### Creating a map
- [new Map(parent, options)](map/mapconstructor.md)
  Creates a map you embed on a webpage and initializes it with the constructor options you choose.
- [interface MapConstructorOptions](mapconstructoroptions.md)
  An object that contains options for creating a map’s features.
### Handling map events
- [Handling map events](handling-map-events.md)
  Register an event lister for events that a map object dispatches.
### Accessing interaction properties
- [isRotationAvailable](map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isRotationEnabled](map/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isScrollEnabled](map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.
### Manipulating the visible portion of the map
- [center](map/center.md)
  The map coordinate at the center of the map view.
- [setCenterAnimated(coordinate, animated)](map/setcenteranimated.md)
  Centers the map to the provided coordinate, with optional animation.
- [region](map/region.md)
  The area the map is displaying.
- [setRegionAnimated(region, animated)](map/setregionanimated.md)
  Changes the map’s region to the provided region, with optional animation.
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
### Showing the map’s controls
- [showsCompass](map/showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [showsMapTypeControl](map/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsScale](map/showsscale.md)
  A feature visibility setting that determines when the map displays the map’s scale indicator.
- [showsUserLocationControl](map/showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](map/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.
### Configuring the map’s appearance
- [colorScheme](map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
- [distances](map/distances-data.property.md)
  The system of measurement that displays on the map.
- [const Distance](distance.md)
  Constants indicating the system of measurement that displays on the map.
- [mapType](map/maptype.md)
  The type of data that the map displays.
- [const MapType](maptype.md)
  Constants representing the type of map to display.
- [padding](map/padding.md)
  The map’s inset margins.
- [pointOfInterestFilter](map/pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
- [showsPointsOfInterest](map/showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [showItems(items, options)](map/showitems.md)
  Adjusts the map’s visible region to bring the specified overlays and annotations into view.
- [interface MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.
### Annotating the map
- [annotations](map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect(mapRect)](map/annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation(annotation)](map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](map/removeannotations.md)
  Removes multiple annotations from the map.
### Adding and removing overlays
- [overlays](map/overlays.md)
  An array of all of the map’s overlays.
- [selectedOverlay](map/selectedoverlay.md)
  The selected overlay on the map.
- [overlaysAtPoint(point)](map/overlaysatpoint.md)
  Returns an array of overlays at a given point on the webpage.
- [addOverlay(overlay)](map/addoverlay.md)
  Adds an overlay to the map.
- [addOverlays(overlays)](map/addoverlays.md)
  Adds multiple overlays to the map.
- [removeOverlay(overlay)](map/removeoverlay.md)
  Removes an overlay from the map.
- [removeOverlays(overlays)](map/removeoverlays.md)
  Removes multiple overlays from the map.
- [topOverlayAtPoint(point)](map/topoverlayatpoint.md)
  Returns the topmost overlay at a given point on the webpage.
### Adding and removing geographical features
- [addItems(items)](map/additems.md)
  Adds a collection of annotations, overlays, or other item collections to the map.
- [removeItems(items)](map/removeitems.md)
  Removes a collection of annotations, overlays, or other item collections from the map.
### Adding and removing tile overlays
- [tileOverlays](map/tileoverlays.md)
  An array of all of the map’s tile overlays.
- [addTileOverlay(tileOverlay)](map/addtileoverlay.md)
  Adds a tile overlay to the map.
- [addTileOverlays(tileOverlays)](map/addtileoverlays.md)
  Adds an array of tile overlays to the map.
- [removeTileOverlay(tileOverlay)](map/removetileoverlay.md)
  Removes a tile overlay from the map.
- [removeTileOverlays(tileOverlays)](map/removetileoverlays.md)
  Removes an array of tile overlays from the map.
### Exploring at street level
- [class LookAround](lookaround.md)
  A view that allows someone to see a street level view of a place.
- [interface LookAroundOptions](lookaroundoptions.md)
  Options for initializing a LookAround view.
- [class LookAroundPreview](lookaroundpreview.md)
  A class that renders a preview of a Look Around view.
- [interface LookAroundPreviewOptions](lookaroundpreviewoptions.md)
  Options for initializing a LookAroundPreview object.
- [class LookAroundScene](lookaroundscene.md)
  Object that represents the current location of the view.
- [interface CommonLookAroundOptions](commonlookaroundoptions.md)
  Options that control the behavior of Look Around views.
### Displaying the user’s location
- [showsUserLocation](map/showsuserlocation.md)
  A Boolean value that determines whether to show the user’s location on the map.
- [tracksUserLocation](map/tracksuserlocation.md)
  A Boolean value that determines whether to center the map on the user’s location.
- [userLocationAnnotation](map/userlocationannotation.md)
  An annotation that indicates the user’s location on the map.
### Converting map coordinates
- [convertCoordinateToPointOnPage(coordinate)](map/convertcoordinatetopointonpage.md)
  Converts a coordinate on the map to a point in the page’s coordinate system.
- [convertPointOnPageToCoordinate(point)](map/convertpointonpagetocoordinate.md)
  Converts a point in page coordinates to the corresponding map coordinate.
### Destroying a map
- [destroy()](map/destroy.md)
  Removes the map’s element from the DOM and releases internal references to the map to free up memory.
### Accessing the element
- [element](map/element.md)
  The map’s DOM element.
### Selecting map features
- [selectableMapFeatures](map/selectablemapfeatures.md)
  An array of map features that users can select from the map.
- [selectableMapFeatureSelectionAccessory](map/selectablemapfeatureselectionaccessory.md)
  An accessory for displaying place information when a person selects a map feature.
- [annotationForMapFeature](map/annotationformapfeature.md)
  The method MapKit JS calls when the framework creates a map feature annotation.
### Prioritizing feature loading
- [loadPriority](map/loadpriority.md)
  A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.
- [const LoadPriority](loadpriority.md)
  Values for prioritizing the visibility of specific map features while the map is loading.
### Static properties
- [ColorSchemes](map/colorschemes.md)
  A static property that allows you to access to access the look color scheme enumeration.
- [Distances](map/distances-data.var.md)
  A static property that allows you to access the distance enumeration.
- [LoadPriorities](map/loadpriorities.md)
  A static property that allows you to access the load priority enumeration.
- [MapTypes](map/maptypes.md)
  A static property that allows you to access the map type enumeration.

## Relationships

### Inherits From
- [MapKitEventTarget](mapkiteventtarget.md)

## See Also

- [maps](mapkit/maps.md)
  An array that automatically adds and removes maps as the framework creates and destroys them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map)*