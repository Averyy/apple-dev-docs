# MapKit

**Framework**: MapKit  
**Kind**: module

Display map or satellite imagery within your app, call out points of interest, and determine placemark information for map coordinates.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Use MapKit to give your app a sense of place with maps and location information. You can use the MapKit framework to:

- Embed maps directly into your app’s windows and views.
- Add annotations and overlays to a map to call out points of interest.
- Add LookAround capabilities to enable users to explore locations at street level.
- Respond to user interactions with well known points of interest, geographical features, and boundaries.
- Provide text completion to make it easy for users to search for a destination or point of interest.

## Topics

### The MapKit APIs
- [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)
- [MapKit for SwiftUI](mapkit-for-swiftui.md)
  MapKit for SwiftUI allows you to build map-centric views and apps across Apple platforms. You can design expressive and highly interactive Maps with minimal code by composing views, using ViewBuilders and view modifiers.
- [Adopting unified Maps URLs](unified-map-urls.md)
  Access Maps URLs and options for displaying Maps information across Apple platforms.
### Articles
- [Deprecated Symbols](mapkit_for_appkit_and_uikit-deprecated-symbols.md)
  MapKit classes, protocols, and entitlements that are no longer supported.
- [Preparing your app to be the default navigation app](preparing-your-app-to-be-the-default-navigation-app.md)
  Configure your navigation app so people can set it as the default on their devices.
### Classes
- [class MKCircleView](mkcircleview.md)
  Provides the visual representation for an [`MKCircle`](mkcircle.md) annotation object.
- [class MKOverlayPathView](mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKOverlayView](mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
- [class MKPolygonView](mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](mkpolygon.md) annotation object.
- [class MKPolylineView](mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](mkpolyline.md) annotation object.
### Structures
- [struct AnyMapContent](anymapcontent.md)
  A type-erased map content.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [MapKit JS](../MapKitJS/MapKitJS.md)
  Embed interactive Apple Maps on your website, annotate points of interest, and perform georelated searches.
- [Apple Maps Server API](../AppleMapsServerAPI/AppleMapsServerAPI.md)
  Reduce API calls and conserve device power by streamlining your app’s georelated searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MapKit)*