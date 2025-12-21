# mapkit

**Framework**: MapKit JS  
**Kind**: class

The JavaScript API for embedding Apple Maps on your website.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapKit extends MapKitEventTarget
```

## Mentions

- [Creating a Maps token](creating-a-maps-token.md)

#### Overview

The [`mapkit`](mapkit.md) object is the main namespace for the MapKit JS framework. Similar to [`MapKit`](https://developer.apple.com/documentation/MapKit) for apps, you can use MapKit JS to display interactive maps with customized annotations and overlays, and provide directions and search services. Your app can supply step-by-step navigation, and help a user find a location by autocompleting a search query.

MapKit JS lets you customize the look of your map. You can choose style details for overlays and annotations, display a standard street map or one that uses satellite imagery, and adjust the visibility of map controls. Additionally, you can customize a map’s behavior by providing event handlers that cause the map to scroll or respond when users select items. You can also enable or disable panning, zooming, and rotation.

## Topics

### Initialization
- [Handling initialization events](handling-initialization-events.md)
  Respond to events that trigger when MapKit JS initializes.
- [init(options)](mapkit/init.md)
  Initializes MapKit JS by providing an authorization callback function and optional language.
- [interface MapKitInitializationOptions](mapkitinitializationoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.
- [load(libraryNames)](mapkit/load.md)
  Tells MapKit JS which libraries to load.
### Maps
- [class Map](map.md)
  An embeddable interactive map that you add to a webpage.
- [maps](mapkit/maps.md)
  An array that automatically adds and removes maps as the framework creates and destroys them.
### Annotations and overlays
- [Annotations](annotations.md)
  Create annotations to add indicators and additional details for specific locations on a map.
- [Overlays](overlays.md)
  Create overlays to highlight geographic regions or paths.
### Geocoder
- [class Geocoder](geocoder.md)
  A geocoder that converts human-readable addresses to geographic coordinates, and vice versa.
### Search
- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [class AddressFilter](addressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [class Search](search.md)
  An object that retrieves map-based search results for a user-entered query.
### Points of interest
- [filterExcludingAllCategories](mapkit/filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [filterIncludingAllCategories](mapkit/filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [class PointOfInterestFilter](pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [class PointsOfInterestSearch](pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const MapFeatureType](mapfeaturetype.md)
  Values that describe the feature type of a point of interest.
### Directions
- [class Directions](directions.md)
  An object that provides directions and estimated travel time based on the options you provide.
### Map view customization
- [class Padding](padding.md)
  The values that define content padding within the map view frame.
- [const FeatureVisibility](featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.
### Geographical features
- [importGeoJSON(data, callback)](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS compatible items.
- [interface GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [type Item](item.md)
  A type alias that represents all objects that the framework sets in an item collection.
- [class ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [type GeoJSONImporterCallback](geojsonimportercallback.md)
  A callback function that MapKit JS invokes when importing a GeoJSON object.
- [class GeoJSONImportError](geojsonimporterror.md)
  An error object that indicates an error occurred while importing a GeoJSON object.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.
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
- [class AbstractLookAround](abstractlookaround.md)
  An abstract class that provides a common interface for Look Around views.
- [lookAroundViews](mapkit/lookaroundviews.md)
  A list of all the Look Around objects that are currently active on a page.
### Places
- [class Place](place.md)
  A place object that returns from a geocoder lookup, a reverse lookup, or a fetch request for points of interest.
- [class PlaceLookup](placelookup.md)
  An object that provides the ability to look up place information for a specified Place ID.
- [placeDetails](mapkit/placedetails.md)
  A list of all place detail objects that are currently active on a page.
- [interface PlaceSelectionAccessoryOptions](placeselectionaccessoryoptions.md)
  The options for selection accessories.
- [class PlaceAnnotation](placeannotation.md)
  An annotation for a place.
- [class PlaceDetail](placedetail.md)
  An interactive view that displays information about a place.
- [class PlaceSelectionAccessory](placeselectionaccessory.md)
  The accessory that conveys information about a place associated with an annotation.
### Map coordinates
- [class Coordinate](coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [class CoordinateRegion](coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [class CoordinateSpan](coordinatespan.md)
  The width and height of a map region.
- [class BoundingRegion](boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.
### Map units
- [class MapPoint](mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [class MapRect](maprect.md)
  A rectangular region, in map units, of a two-dimensional map projection.
- [class MapSize](mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.
- [class CameraZoomRange](camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.
### Version and language
- [language](mapkit/language.md)
  A language ID indicating the selected language.
- [build](mapkit/build.md)
  The build string.
- [version](mapkit/version.md)
  The version of MapKit JS.
### Setting images
- [type ImageHashObject](imagehashobject.md)
  An object that defines a set of images URLs for different scales.
- [interface ImageDelegate](imagedelegate.md)
  An object you use to specify image URLs.
### Service
- [class Service](service.md)
  An abstract class that provides common interfaces for service objects.
### Events
- [class MapKitEvent](mapkitevent.md)
  A generic MapKit JS event object.
- [type MapKitEventListener](mapkiteventlistener.md)
  A type alias that represents a function or an object that receives a MapKit event.
- [class MapKitEventTarget](mapkiteventtarget.md)
  An abstract class that defines the interface for objects that can dispatch events.
### Namespace properties
- [AddressCategory](mapkit/addresscategory.md)
  The getter to use to access the address category enumeration.
- [AddressFilter](mapkit/addressfilter.md)
  The getter to use to access the address filter class.
- [Annotation](mapkit/annotation.md)
  The getter to use to for access the annotation class.
- [BoundingRegion](mapkit/boundingregion.md)
  The getter to use to access the the bounding region class.
- [CameraZoomRange](mapkit/camerazoomrange.md)
  The getter to use to access the camera zoom range class.
- [CircleOverlay](mapkit/circleoverlay.md)
  The getter to use to access the circle overlay class.
- [Coordinate](mapkit/coordinate.md)
  The getter to use to access the coordinate class.
- [CoordinateRegion](mapkit/coordinateregion.md)
  The getter to use to access the coordinate region class.
- [CoordinateSpan](mapkit/coordinatespan.md)
  The getter to use to access the coordinate span class.
- [Directions](mapkit/directions.md)
  The getter to use to access the directions class.
- [FeatureVisibility](mapkit/featurevisibility.md)
  The getter to use to access the feature-visibility enumeration.
- [Geocoder](mapkit/geocoder.md)
  The getter to use to access the geocoder class.
- [ImageAnnotation](mapkit/imageannotation.md)
  The getter to use to access the image annotation class.
- [LineGradient](mapkit/linegradient.md)
  The getter to use to access the line gradient class.
- [LookAround](mapkit/lookaround.md)
  The getter to use to access the look around class.
- [LookAroundPreview](mapkit/lookaroundpreview.md)
  The getter to use to access the look around preview class.
- [LookAroundScene](mapkit/lookaroundscene.md)
  The getter to use to access the look around scene class.
- [Map](mapkit/map.md)
  The getter to use to access the map view class.
- [MapFeatureAnnotation](mapkit/mapfeatureannotation.md)
  The getter to use to access the map feature annotation class.
- [MapFeatureType](mapkit/mapfeaturetype.md)
  The getter to use to access the map feature type enumeration.
- [MapPoint](mapkit/mappoint.md)
  The getter to use to access the map point class.
- [MapRect](mapkit/maprect.md)
  The getter to use to access the map rect class.
- [MapSize](mapkit/mapsize.md)
  The getter to use to access the map size class.
- [MarkerAnnotation](mapkit/markerannotation.md)
  The getter to use to access the marker annotation class.
- [Padding](mapkit/padding.md)
  The getter to use to access the padding class.
- [Place](mapkit/place.md)
  The getter to use to access the place class.
- [PlaceAnnotation](mapkit/placeannotation.md)
  The getter to use to access the place annotation class.
- [PlaceDetail](mapkit/placedetail.md)
  The getter to use to access the place detail class.
- [PlaceLookup](mapkit/placelookup.md)
  The getter to use to access the place lookup class.
- [PlaceSelectionAccessory](mapkit/placeselectionaccessory.md)
  The getter to use to access the place selection accessory class.
- [PointOfInterestCategory](mapkit/pointofinterestcategory.md)
  The getter to use to access the point-of-interest category enumeration.
- [PointOfInterestFilter](mapkit/pointofinterestfilter.md)
  The getter to use to access the point-of-interest filter class.
- [PointsOfInterestSearch](mapkit/pointsofinterestsearch.md)
  The getter to use to access the points of interest search class.
- [PolygonOverlay](mapkit/polygonoverlay.md)
  The getter to use to access the polygon overlay class.
- [PolylineOverlay](mapkit/polylineoverlay.md)
  The getter to use to access the polyline overlay class.
- [Search](mapkit/search.md)
  The getter to use to access the search class.
- [SearchAutocompleteResult](mapkit/searchautocompleteresult.md)
  The getter to use to access the search autocomplete result class.
- [Style](mapkit/style.md)
  The getter to use to access the style class.
- [TileOverlay](mapkit/tileoverlay.md)
  The getter to use to access the tile overlay class.

## Relationships

### Inherits From
- [MapKitEventTarget](mapkiteventtarget.md)

## See Also

- [Displaying place information using the Maps Embed API](displaying-place-information-using-the-maps-embed-api.md)
  Show place information on a map using a URL.
- [Creating a Maps token](creating-a-maps-token.md)
  Generate your token to access MapKit services with proper authorization.
- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
  Link to the most recent autoupdating version of MapKit JS, or a version of your choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit)*