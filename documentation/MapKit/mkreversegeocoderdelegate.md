# MKReverseGeocoderDelegate

**Framework**: MapKit  
**Kind**: protocol  
**Role**: Protocol

Defines the interface for receiving messages from an [`MKReverseGeocoder`](./mkreversegeocoder.md) object.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```objc
@protocol MKReverseGeocoderDelegate <NSObject>
```

#### Overview

You use this protocol to receive the placemark information for a given coordinate or to retrieve any errors that occurred during the reverse-geocoding process.

Delegates must implement both methods of this protocol.

The Google terms of service require that the reverse geocoding service be used in conjunction with a Google map; take this into account when designing your application’s user interface.

Each Map Kit application has a limited amount of reverse geocoding capacity, so it is to your advantage to use reverse geocode requests sparingly. For more information about when to initiate reverse-geocoding requests, see [`MKReverseGeocoder`](./mkreversegeocoder.md).

This protocol is deprecated in iOS 5.0. Use the [`CLGeocoder`](../CoreLocation/clgeocoder.md) class instead.

## Topics

### Processing placemark searches
- [- reverseGeocoder:didFindPlacemark:](./mkreversegeocoderdelegate/reversegeocoder_didfindplacemark_.md)
  Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate.
- [- reverseGeocoder:didFailWithError:](./mkreversegeocoderdelegate/reversegeocoder_didfailwitherror_.md)
  Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate)*