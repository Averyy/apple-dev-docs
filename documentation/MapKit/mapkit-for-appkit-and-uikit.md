# MapKit for AppKit and UIKit

**Framework**: MapKit

## Topics

### Essentials
- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md)
  Configure your routing app to support providing directions.
- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapView](mkmapview.md)
  An embeddable map interface, similar to the one that the Maps app provides.
- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.
### Map coordinates
- [struct MKCoordinateRegion](mkcoordinateregion.md)
  A rectangular geographic region that centers around a specific latitude and longitude.
- [struct MKCoordinateSpan](mkcoordinatespan.md)
  The width and height of a map region.
- [struct MKMapRect](mkmaprect.md)
  A rectangular area on a two-dimensional map projection.
- [struct MKMapPoint](mkmappoint.md)
  A point on a two-dimensional map projection.
- [struct MKMapSize](mkmapsize.md)
  Width and height information on a two-dimensional map projection.
- [class MKDistanceFormatter](mkdistanceformatter.md)
  A utility object that converts between a geographic distance and a string-based expression of that distance.
### Map customization
- [class MKMapCamera](mkmapcamera.md)
  A virtual camera for defining the appearance of the map.
- [class MKCompassButton](mkcompassbutton.md)
  A specialized view that displays the compass heading for its associated map.
- [class MKScaleView](mkscaleview.md)
  A specialized view that displays the scale information for its associated map.
- [class MKZoomControl](mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingButton](mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [class MKUserTrackingBarButtonItem](mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.
### Annotations and overlays
- [MapKit annotations](mapkit-annotations.md)
  Create annotations to add indicators and additional details for specific locations on a map.
- [MapKit overlays](mapkit-overlays.md)
  Create overlays to highlight geographic regions or paths.
### Directions
- [class MKDirections](mkdirections.md)
  A utility object that computes directions and travel-time information based on the route information you provide.
- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.
### Geographical features
- [Displaying an Indoor Map](displaying-an-indoor-map.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [class MKGeoJSONDecoder](mkgeojsondecoder.md)
  An object that decodes GeoJSON objects into MapKit types.
- [class MKGeoJSONFeature](mkgeojsonfeature.md)
  The decoded representation of a GeoJSON feature.
- [protocol MKGeoJSONObject](mkgeojsonobject.md)
  Objects that the GeoJSON decoder can return.
### Local search
- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md)
  Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [enum MKLocalSearchRegionPriority](mklocalsearchregionpriority.md)
  A value that indicates the importance of the configured region.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.
- [class MKLocalSearch](mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class MKAddressFilter](mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.
### Exploring at street level
- [class MKLookAroundScene](mklookaroundscene.md)
  A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [class MKLookAroundSceneRequest](mklookaroundscenerequest.md)
  A class you use to request a LookAround scene at the location you specify.
- [class MKLookAroundViewController](mklookaroundviewcontroller.md)
  A class that manages the presentation and display of a LookAround view.
- [class MKLookAroundSnapshotter](mklookaroundsnapshotter.md)
  A utility class that you use to create a static image from a LookAround scene.
### Place information
- [protocol MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md)
  The methods that you use to receive events from an associated map view controller.
- [class MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md)
  An object that displays detailed information about a map item.
- [MKSelectionAccessory.MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md)
  The type of map item detail accessory presentation to use.
- [class MKSelectionAccessory](mkselectionaccessory.md)
  The type of accessory to display for a selected annotation.
- [MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md)
  The style to use for a map item detail callout presentation.
### Points of interest
- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapFeatureAnnotation](mkmapfeatureannotation.md)
  A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [struct MKMapFeatureOptions](mkmapfeatureoptions.md)
  A structure you use to tell the map which kinds of features users can interact with.
- [class MKMapItemRequest](mkmapitemrequest.md)
  A utility class you use to request additional information about a map feature.
- [class MKIconStyle](mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [class MKPointOfInterestFilter](mkpointofinterestfilter.md)
  A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [struct MKPointOfInterestCategory](mkpointofinterestcategory.md)
  A point of interest category.
### Static map snapshots
- [class MKMapSnapshotter](mkmapsnapshotter.md)
  A utility class for capturing a map and its content into an image.
- [MKMapSnapshotter.Snapshot](mkmapsnapshotter/snapshot.md)
  An image that a snapshotter object generates.
### Reference
- [MapKit Functions](mapkit-functions.md)
  The functions of the MapKit framework provide convenient ways to package map-related data structures.
### Errors
- [let MKErrorDomain: String](mkerrordomain.md)
  The error domain for MapKit.
- [struct MKError](mkerror.md)
  Error constants for the MapKit framework.
- [MKError.Code](mkerror/code.md)
  Error constants for the MapKit framework.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Map protocols and view modifiers that are no longer supported.

## See Also

- [MapKit for SwiftUI](mapkit-for-swiftui.md)
  MapKit for SwiftUI allows you to build map-centric views and apps across Apple platforms. You can design expressive and highly interactive Maps with minimal code by composing views, using ViewBuilders and view modifiers.
- [Adopting unified Maps URLs](unified-map-urls.md)
  Access Maps URLs and options for displaying Maps information across Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapkit-for-appkit-and-uikit)*