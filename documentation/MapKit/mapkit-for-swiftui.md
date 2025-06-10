# MapKit for SwiftUI

**Framework**: MapKit

MapKit for SwiftUI allows you to build map-centric views and apps across Apple platforms. You can design expressive and highly interactive Maps with minimal code by composing views, using ViewBuilders and view modifiers.

#### Overview

Like MapKit for AppKit and UIKit, MapKit for SwiftUI allows you to take advantage of map styles ranging from satellite imagery to rich, 3D perspective imagery to present vivid maps. Using [`MapContentBuilder`](mapcontentbuilder.md) you can configure your maps to show [`Marker`](marker.md) and [`Annotation`](annotation.md) views, or — for more specialized content — you can design your own SwiftUI views to place on the map. To add even more interactivity, MapKit for SwiftUI supports overlays to highlight areas on the map, enabling you to animate paths and directions using [`MapPolyline`](mappolyline.md), or make it easy for people to dig deeper into on the ground details with tappable points of interest. People who use your app can also explore at street level using [`LookAroundPreview`](lookaroundpreview.md) and Look Around viewer.

> **Note**:  For more information about integrating MapKit into your app using SwiftUI, see WWDC23 session 10043: [`Meet MapKit for SwiftUI`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10043/)

## Topics

- [Searching, displaying, and navigating to places](searching-displaying-and-navigating-to-places.md)
  Convert place information between coordinates and user-friendly place names, get cycling directions, and conveniently display formatted addresses.
### Essentials
- [struct Map](map.md)
  A view that displays an embedded map interface.
- [struct MapStyle](mapstyle.md)
  A style that you can apply to a map.
### Annotations and overlays
- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.
### Map controls
- [struct MapCompass](mapcompass.md)
  A view that reflects the current orientation of the associated map.
- [struct MapLocationCompass](maplocationcompass.md)
  A view that displays a combined user location button and map compass.
- [struct MapPitchSlider](mappitchslider.md)
  A slider control that allows a person to change the pitch of the map.
- [struct MapPitchToggle](mappitchtoggle.md)
  A button that sets the pitch of the associated map.
- [struct MapScaleView](mapscaleview.md)
  Displays a legend with distance information for the associated map.
- [struct MapUserLocationButton](mapuserlocationbutton.md)
  A button that sets the framing of the associated map to the user location.
- [struct MapZoomStepper](mapzoomstepper.md)
  Buttons a person uses to adjust the zoom level of the map.
### Exploring at street level
- [struct LookAroundPreview](lookaroundpreview.md)
  A view that provides a Look Around preview for a specific geographic location.
### Map features
- [struct MapFeature](mapfeature.md)
  A tappable map feature.
- [struct MapSelection](mapselection.md)
  A value representing a selected feature on a map.
- [protocol MapSelectable](mapselectable.md)
### Map customization
- [struct MapCamera](mapcamera.md)
  Defines a virtual viewpoint above the map surface.
- [struct MapCameraBounds](mapcamerabounds.md)
  Defines an optional boundary of an area within which the map’s center needs to remain.
- [struct MapCameraPosition](mapcameraposition.md)
  A structure that describes how to position the map’s camera within the map.
- [struct MapCameraUpdateContext](mapcameraupdatecontext.md)
  A structure that defines additional information about the map camera.
- [struct MapCameraUpdateFrequency](mapcameraupdatefrequency.md)
  A structure that describes when the map camera updates.
### Place information
- [struct MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle.md)
  The map item detail selection accessory style.
- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](mapcontent/mapitemdetailselectionaccessory(_:).md)
  Specifies the selection accessory to display for the selected map item content.
- [static func callout(MapItemDetailSelectionAccessoryStyle.CalloutStyle) -> MapItemDetailSelectionAccessoryStyle](mapitemdetailselectionaccessorystyle/callout(_:).md)
  Presents the accessory as an annotation callout on the map.
### Geocoding
- [class MKGeocodingRequest](mkgeocodingrequest.md)
  A class that looks up a geographic coordinate using the provided string.
- [class MKReverseGeocodingRequest](mkreversegeocodingrequest.md)
  A class that looks up address strings for the provided geographic coordinates.
### Representing places and addresses
- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.
- [class MKAddress](mkaddress.md)
  A class that contains a full address, and, optionally, a short address.
- [class MKAddressRepresentations](mkaddressrepresentations.md)
  A class that provides formatted address strings.
- [GeoToolbox](../GeoToolbox/GeoToolbox.md)
  Determine place descriptor information for map coordinates.
### Points of interest
- [struct PointOfInterestCategories](pointofinterestcategories.md)
  A structure you use to define points of interest to include or exclude on a map.
### Protocols
- [protocol DynamicMapContent](dynamicmapcontent.md)
  A  type of view that generates views from an underlying collection of data.
- [protocol MapContent](mapcontent.md)
  A protocol used to construct map content such as controls, markers, and annotations.
- [struct MapContentBuilder](mapcontentbuilder.md)
  A result builder that creates map content from closures you provide.
- [struct MapContentView](mapcontentview.md)
  A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.
### Structures
- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapProxy](mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct MapReader](mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](mapselectablecontentview.md)

## See Also

- [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)
- [Adopting unified Maps URLs](unified-map-urls.md)
  Access Maps URLs and options for displaying Maps information across Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapkit-for-swiftui)*