# mapkit

**Framework**: MapKit JS  
**Kind**: class

The JavaScript API for embedding Apple Maps on your website.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit
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
- [init](mapkit/init.md)
  Initializes MapKit JS by providing an authorization callback function and optional language.
- [MapKitInitOptions](mapkitinitoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.
- [load](mapkit/load.md)
  Tells MapKit JS which libraries to load.
- [addEventListener](mapkit/addeventlistener.md)
  Subscribes a listener function to an event type.
- [removeEventListener](mapkit/removeeventlistener.md)
  Unsubscribes a listener function from an event type.
### Maps
- [mapkit.Map](mapkit.map.md)
  An embeddable interactive map that you add to a webpage.
- [maps](mapkit/maps.md)
  An array that automatically adds and removes maps as the framework creates and destroys them.
### Annotations and overlays
- [Annotations](annotations.md)
  Create annotations to add indicators and additional details for specific locations on a map.
- [Overlays](overlays.md)
  Create overlays to highlight geographic regions or paths.
### Geocoder
- [mapkit.Geocoder](mapkit.geocoder.md)
  A geocoder that converts human-readable addresses to geographic coordinates, and vice versa.
### Search
- [mapkit.AddressCategory](mapkit.addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [mapkit.AddressFilter](mapkit.addressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [mapkit.Search](mapkit.search.md)
  An object that retrieves map-based search results for a user-entered query.
### Points of interest
- [mapkit.filterExcludingAllCategories](mapkit/mapkit.filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [mapkit.filterIncludingAllCategories](mapkit/mapkit.filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [mapkit.PointOfInterestFilter](mapkit.pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [mapkit.PointsOfInterestSearch](mapkit.pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [mapkit.MapFeatureAnnotationGlyphImage](mapkit.mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [mapkit.PointOfInterestCategory](mapkit.pointofinterestcategory.md)
  Point-of-interest categories.
- [mapkit.MapFeatureType](mapkit.mapfeaturetype.md)
  Values that describe the feature type of a point of interest.
### Directions
- [mapkit.Directions](mapkit.directions.md)
  An object that provides directions and estimated travel time based on the options you provide.
### Map view customization
- [mapkit.Padding](mapkit.padding.md)
  The values that define content padding within the map view frame.
- [mapkit.FeatureVisibility](mapkit.featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.
### Geographical features
- [importGeoJSON](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS items.
- [GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.
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
### Places
- [Place](place.md)
  A place object that returns from a geocoder lookup, a reverse lookup, or a fetch request for points of interest.
- [PlaceDetailOptions](placedetailoptions.md)
- [mapkit.PlaceLookup](mapkit.placelookup.md)
  An object that provides the ability to look up place information for a specified Place ID.
- [placeDetails](mapkit/placedetails.md)
  A list of all user-created place detail objects that are currently active on a page.
- [PlaceLookupOptions](placelookupoptions.md)
  The options for creating a place lookup.
- [PlaceSelectionAccessoryOptions](placeselectionaccessoryoptions.md)
  The options for selection accessories.
- [mapkit.PlaceAnnotation](mapkit.placeannotation.md)
  An annotation for a place.
- [mapkit.PlaceDetail](mapkit.placedetail.md)
  An interactive view that displays information about a place.
- [mapkit.PlaceSelectionAccessory](mapkit.placeselectionaccessory.md)
  The accessory that conveys information about a place associated with an annotation.
### Map coordinates
- [mapkit.Coordinate](mapkit.coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [mapkit.CoordinateRegion](mapkit.coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [mapkit.CoordinateSpan](mapkit.coordinatespan.md)
  The width and height of a map region.
- [mapkit.BoundingRegion](mapkit.boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.
### Map units
- [mapkit.MapPoint](mapkit.mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [mapkit.MapRect](mapkit.maprect.md)
  A rectangular region, in map units, of a two-dimensional map projection.
- [mapkit.MapSize](mapkit.mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.
- [mapkit.CameraZoomRange](mapkit.camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.
### Version and language
- [language](mapkit/language.md)
  A language ID indicating the selected language.
- [build](mapkit/build.md)
  The build string.
- [version](mapkit/version.md)
  The version of MapKit JS.
### Response objects
- [FetchResponse](fetchresponse.md)
  An object that contains data MapKit JS returns from a place search request.
### Delegates
- [FetchDelegate](fetchdelegate.md)
  An object to pass to a map feature annotation to fetch place objects instead of a callback function.
- [ImageDelegate](imagedelegate.md)
  An object you use to specify image URLs.

## See Also

- [Displaying place information using the Maps Embed API](displaying-place-information-using-the-maps-embed-api.md)
  Show place information on a map using a URL.
- [Creating a Maps token](creating-a-maps-token.md)
  Generate your token to access MapKit services with proper authorization.
- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
  Link to the most recent autoupdating version of MapKit JS, or a version of your choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit)*