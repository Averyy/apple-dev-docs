# Apple Maps Server API

**Framework**: Apple Maps Server API  
**Kind**: module

Reduce API calls and conserve device power by streamlining your app’s georelated searches.

**Availability**:
- Apple Maps Server API 1.2+

#### Overview

Use this web-based service to streamline your app’s API by moving georelated searches for places, points of interest, geocoding, directions, possible autocompletions for searches, and estimated time of arrival (ETA) calculations from inside your app to your server.

To try the Maps Server API, generate a temporary token as described in [`Creating a Maps token`](https://developer.apple.com/documentation/MapKitJS/creating-a-maps-token). Use these credentials to access the API from your app, or use them on [`Try Maps Server API`](https://developer.apple.comhttps://developer.apple.com/maps/try-maps-server-api/).

The Apple Maps Server API is a web-based API similar to the [`MapKit JS`](https://developer.apple.com/documentation/MapKitJS) API, and uses the same authorization infrastructure. It requires authorization using a JSON Web Token (JWT) for API calls. You obtain a key for creating the token when you complete the setup in your Apple Developer account.

To start using the API, you first need to generate an identifier and a private key, and authenticate with the service, following the steps below:

- To create an identifier and private key, follow the steps in [`Creating a Maps identifier and a private key`](creating-a-maps-identifier-and-a-private-key.md).
- To create tokens from your identifier and private key with the Apple Maps Server API, follow the steps in [`Creating and using tokens with Maps Server API`](creating-and-using-tokens-with-maps-server-api.md).
- Use the Token API to [`Generate a Maps token`](-v1-token.md) for API access.

The service provides up to 25,000 service calls per day per team between Apple Maps Server API and MapKit JS. If your app exceeds this quota, the service returns an HTTP 429 error (Too Many Requests) and your app needs to retry later. If your app requires a larger daily quota, submit a [`quota increase request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/mapkitjs/).

## Topics

### Essentials
- [Creating and using tokens with Maps Server API](creating-and-using-tokens-with-maps-server-api.md)
  Sign JSON Web Tokens to use Maps Server API and debug common signing errors.
- [Creating a Maps identifier and a private key](creating-a-maps-identifier-and-a-private-key.md)
  Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Generate a Maps token](-v1-token.md)
  Returns a JWT maps access token that you use to call the service API.
- [Debugging an Invalid token](debugging-an-invalid-token.md)
  Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.
- [Common objects](common-objects.md)
  Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](integrating-the-apple-maps-server-api-into-java-server-applications.md)
  Streamline your app’s API by moving georelated searches from inside your app to your server.
### Geocoding
- [Geocode an address](-v1-geocode.md)
  Returns the latitude and longitude of the address you specify.
- [Reverse geocode a location](-v1-reversegeocode.md)
  Returns an array of addresses present at the coordinates you provide.
### Searching
- [type AddressCategory](addresscategory.md)
  Search categories related to political geographical boundaries.
- [type SearchACResultType](searchacresulttype.md)
  An enumerated string that indicates the result type for the search request.
- [type SearchResultType](searchresulttype.md)
  An enumerated string that indicates the result type for the search autocomplete request.
- [object AlternateIdsResponse](alternateidsresponse.md)
  A list of alternate Place IDs and associated errors.
- [object AlternateIdsResponse.AlternateIds](alternateidsresponse/alternateids.md)
  Contains a list of alternate Place IDs for a given Place ID.
- [object PlacesResponse](placesresponse.md)
  A list of Place IDs and errors.
- [object PlacesResponse.PlaceLookupError](placesresponse/placelookuperror.md)
  An error associated with a lookup call.
- [Search for places that match specific criteria](-v1-search.md)
  Find places by name or by specific search criteria.
- [Search for places that meet specific criteria to autocomplete a place search](-v1-searchautocomplete.md)
  Find results that you can use to autocomplete searches.
- [Search for a place using an identifier](-v1-place-:id.md)
  Obtain a Place object for a given Place ID.
- [Search for places using mulitple identifiers](-v1-place.md)
  Obtain a set of Place objects for a given set of Place IDs.
- [Obtain a list of alternate place identifiers](-v1-place-alternateids.md)
  Get a list of alternate Place IDs given one or more Place IDs.
### Directions
- [Search for directions and estimated travel time between locations](-v1-directions.md)
  Find directions by specific criteria.
- [Determine estimated arrival times and distances to one or more destinations](-v1-etas.md)
  Returns the estimated time of arrival (ETA) and distance between starting and ending locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleMapsServerAPI)*