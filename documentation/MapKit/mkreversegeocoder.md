# MKReverseGeocoder

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

Provides services for converting a map coordinate (specified as a latitude/longitude pair) into information about that coordinate, such as the country or region, city, or street.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```objc
@interface MKReverseGeocoder : NSObject
```

#### Overview

A reverse geocoder object is a single-shot object that works with a network-based map service to look up placemark information for its specified coordinate value.

The Google terms of service require that the reverse geocoding service be used in conjunction with a Google map; take this into account when designing your application’s user interface.

Each Map Kit application has a limited amount of reverse geocoding capacity, so it is to your advantage to use reverse geocode requests sparingly. Here are some rules of thumb for using this class most effectively:

- Send at most one reverse-geocoding request for any one user action.
- If the user performs multiple actions that involve reverse-geocoding the same location, reuse the results from the initial reverse-geocoding request instead of starting individual requests for each action.
- When you want to update the location automatically (such as when the user is moving), reissue the reverse-geocoding request only when the user’s location has moved a significant distance and after a reasonable amount of time has passed. For example, in a typical situation, you should not send more than one reverse-geocode request per minute.
- Do not start a reverse-geocoding request at a time when the user will not see the results immediately. For example, do not start a request if your application recently resigned the active state (possibly because of an interruption such as a phone call) and is waiting to become active again.

An iOS-based device must have access to the network in order for the reverse geocoder object to return valid information. The reverse geocoder returns information through its associated delegate object, which is an object that conforms to the [`MKReverseGeocoderDelegate`](./mkreversegeocoderdelegate.md) protocol. If the reverse geocoder is unable to retrieve the requested information, it similarly reports the error to its delegate object. For more information on this protocol, see [`MKReverseGeocoderDelegate`](./mkreversegeocoderdelegate.md).

This class is deprecated in iOS 5.0. Use the [`CLGeocoder`](../CoreLocation/clgeocoder.md) class instead.

## Topics

### Initializing the Reverse Geocoder
- [- initWithCoordinate:](./mkreversegeocoder/initwithcoordinate_.md)
  Initializes the reverse geocoder with the specified coordinate value.
### Accessing Reverse Geocoder Attributes
- [delegate](./mkreversegeocoder/delegate.md)
  The reverse geocoder’s delegate object.
- [coordinate](./mkreversegeocoder/coordinate.md)
  The coordinate whose placemark data you want to retrieve.
- [placemark](./mkreversegeocoder/placemark.md)
  The result of the reverse-geocoding operation.
### Managing the Search
- [- start](./mkreversegeocoder/start.md)
  Starts the reverse-geocoding process asynchronously.
- [querying](./mkreversegeocoder/querying.md)
  A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate.
- [- cancel](./mkreversegeocoder/cancel.md)
  Cancels a pending reverse-geocoding request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Classes
- [class MKCircleView](./mkcircleview.md)
  Provides the visual representation for an [`MKCircle`](./mkcircle.md) annotation object.
- [class MKOverlayView](./mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
- [class MKOverlayPathView](./mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKPolygonView](./mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](./mkpolygon.md) annotation object.
- [class MKPolylineView](./mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](./mkpolyline.md) annotation object.
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder)*