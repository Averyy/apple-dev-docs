# mapkit.Geocoder

**Framework**: MapKit JS  
**Kind**: class

A geocoder that converts human-readable addresses to geographic coordinates, and vice versa.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Geocoder
```

#### Overview

When using MapKit JS to show Apple Maps on a website, the geocoder handles forward and reverse geocoding. Because the framework performs geocoding on the server, the geocoder requires a network connection and handles calls asynchronously.

Provide context to the geocoder to get the most relevant results. The geocoder can obtain context from these sources:

-  The geocoder assigns higher relevancy to results near the user’s location. Asking for the user’s location requires the user’s permission. If you enable this option, the browser asks the user for permission (some browsers remember this setting for a day). MapKit JS disables this option by default.
-  Your website can provide context in the geocoder lookup options as a coordinate or region. For example, if a user types  into a map text field and the web page invokes the geocoder without context, the geocoder returns the major city in Australia. If, however, the map displays San Francisco and its environs, a geocoding request with this region as context returns the nearby city of Brisbane instead.
-  Of the three forms of context, this is the least accurate, but the only one certain to be present. The user’s IP address is a granular IP location that the system doesn’t log or store.

## Topics

### Creating a geocoder object
- [mapkit.Geocoder](mapkit.geocoder/mapkit.geocoder.md)
  Creates a geocoder object and sets optional language and user location properties.
- [GeocoderConstructorOptions](geocoderconstructoroptions.md)
  Initialization options for geocoder objects.
- [getsUserLocation](mapkit.geocoder/getsuserlocation.md)
  A Boolean value that indicates whether the geocoder returns results near the user’s location.
- [language](mapkit.geocoder/language.md)
  A language ID that determines the language to use for displaying addresses.
### Getting geocoder results
- [lookup](mapkit.geocoder/lookup.md)
  Converts an address to geographic coordinates.
- [GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [reverseLookup](mapkit.geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.
### Canceling a geocoder request
- [cancel](mapkit.geocoder/cancel.md)
  Cancels the pending lookup or reverse lookup using its request ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.geocoder)*