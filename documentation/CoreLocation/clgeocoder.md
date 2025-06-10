# CLGeocoder

**Framework**: Core Location  
**Kind**: class

An interface for converting between geographic coordinates and place names.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CLGeocoder
```

## Mentions

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Overview

The [`CLGeocoder`](clgeocoder.md) class provides services for converting between a coordinate (specified as a latitude and longitude) and the user-friendly representation of that coordinate. A user-friendly representation of the coordinate typically consists of the street, city, state, and country or region information corresponding to the given location, but it may also contain a relevant point of interest, landmarks, or other identifying information. A geocoder object is a single-shot object that works with a network-based service to look up placemark information for its specified coordinate value.

To use a geocoder object, you create it and call one of its forward- or reverse-geocoding methods to begin the request.  requests take a latitude and longitude value and find a user-readable address.  requests take a user-readable address and find the corresponding latitude and longitude value. Forward-geocoding requests may also return additional information about the specified location, such as a point of interest or building at that location. For both types of request, the results are returned using a [`CLPlacemark`](clplacemark.md) object. In the case of forward-geocoding requests, multiple placemark objects may be returned if the provided information yielded multiple possible locations.

To make smart decisions about what types of information to return, the geocoder server uses all the information provided to it when processing the request. For example, if the user is moving quickly along a highway, it might return the name of the overall region, and not the name of a small park that the user is passing through.

##### Tips for Using a Geocoder Object

Apps must be conscious of how they use geocoding. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. (When the maximum rate is exceeded, the geocoder returns an error object with the [`CLError.Code.network`](clerror-swift.struct/code/network.md) error to the associated completion handler.) Here are some rules of thumb for using this class effectively:

- Send at most one geocoding request for any one user action.
- If the user performs multiple actions that involve geocoding the same location, reuse the results from the initial geocoding request instead of starting individual requests for each action.
- When you want to update the user’s current location automatically (such as when the user is moving), issue new geocoding requests only when the user has moved a significant distance and after a reasonable amount of time has passed. For example, in a typical situation, you should not send more than one geocoding request per minute.
- Do not start a geocoding request at a time when the user will not see the results immediately. For example, do not start a request if your application is inactive or in the background.

The computer or device must have access to the network in order for the geocoder object to return detailed placemark information. Although, the geocoder stores enough information locally to report the localized country or region name and ISO country code for many locations. If this information isn’t available for a specific location, the geocoder may still report an error to your completion block.

You can use geocoder objects either in conjunction with, or independent of, the classes of the [`MapKit`](https://developer.apple.com/documentation/MapKit) framework.

## Topics

### Reverse geocoding a location
- [func reverseGeocodeLocation(CLLocation, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/reversegeocodelocation(_:preferredlocale:completionhandler:).md)
  Submits a reverse-geocoding request for the specified location and locale.
- [func reverseGeocodeLocation(CLLocation, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/reversegeocodelocation(_:completionhandler:).md)
  Submits a reverse-geocoding request for the specified location.
- [typealias CLGeocodeCompletionHandler](clgeocodecompletionhandler.md)
  A block to be called when a geocoding request is complete.
### Geocoding an address
- [func geocodeAddressString(String, in: CLRegion?, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified address string and locale information.
- [func geocodeAddressString(String, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified string.
- [func geocodeAddressString(String, in: CLRegion?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:in:completionhandler:).md)
  Submits a forward-geocoding request using the specified string and region information.
- [func geocodePostalAddress(CNPostalAddress, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodepostaladdress(_:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified Contacts framework information.
- [func geocodePostalAddress(CNPostalAddress, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodepostaladdress(_:preferredlocale:completionhandler:).md)
  Submits a forward-geocoding requesting using the specified locale and Contacts framework information.
- [func geocodeAddressDictionary([AnyHashable : Any], completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressdictionary(_:completionhandler:).md)
  Submits a forward-geocoding request using the specified address dictionary.
### Managing geocoding requests
- [func cancelGeocode()](clgeocoder/cancelgeocode.md)
  Cancels a pending geocoding request.
- [var isGeocoding: Bool](clgeocoder/isgeocoding.md)
  A Boolean value indicating whether the receiver is in the middle of geocoding its value.
### Instance Methods
- [func geocodeAddressString(String, inRegionCenteredAt: CLLocationCoordinate2D, inRegionRadius: CLLocationDistance, preferredLocale: Locale?, completionHandler: ([CLPlacemark]?, (any Error)?) -> Void)](clgeocoder/geocodeaddressstring(_:inregioncenteredat:inregionradius:preferredlocale:completionhandler:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
  Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [class CLPlacemark](clplacemark.md)
  A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder)*