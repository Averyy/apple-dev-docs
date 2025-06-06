# Deprecated Symbols

**Framework**: MapKit

MapKit classes, protocols, and entitlements that are no longer supported.

## Topics

### Classes
- [class MKCircleView](mkcircleview.md)
  Provides the visual representation for an [`MKCircle`](mkcircle.md) annotation object.
- [class MKOverlayView](mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
- [class MKOverlayPathView](mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKPolygonView](mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](mkpolygon.md) annotation object.
- [class MKPolylineView](mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](mkpolyline.md) annotation object.
- [class MKPinAnnotationView](mkpinannotationview.md)
  An annotation view that displays a pin image on the map.
### Properties
- [var filterType: MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [var pinColor: MKPinAnnotationColor](mkpinannotationview/pincolor.md)
  The color of the pin head.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var showsPointsOfInterest: Bool](mkmapsnapshotter/options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var mapType: MKMapType](mkmapsnapshotter/options/maptype.md)
  The map’s visual style.
### Methods
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.
### Protocols
- [struct MapPin](mappin.md)
  A pin-shaped annotation used to indicate a location on a map.
### Enumerations
- [MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [enum MKPinAnnotationColor](mkpinannotationcolor.md)
  The supported colors for pin annotations.
### Entitlements
- [Maps Entitlement](../BundleResources/Entitlements/com.apple.developer.maps.md)
  A Boolean value that indicates whether the app may provide directions beyond what Maps supports, such as subway routes, hiking trails, and bike paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapkit_for_appkit_and_uikit-deprecated-symbols)*