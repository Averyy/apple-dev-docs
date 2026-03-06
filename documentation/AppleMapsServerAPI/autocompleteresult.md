# AutocompleteResult

**Framework**: Apple Maps Server API  
**Kind**: dictionary

An object that contains information you can use to suggest addresses and further refine search results.

**Availability**:
- Apple Maps Server API 1.2+

## Declaration

```swift
object AutocompleteResult
```

#### Discussion

If available, the service encodes opaque data about the autocomplete result in the completion URL’s `metadata` parameter. If you need to fetch the search result in a certain language, you need to specify it in the `lang` parameter in the request.

## Properties

- `completionUrl` (string): The relative URI to the `search` endpoint to use to fetch more details pertaining to the result. If available, the framework encodes opaque data about the autocomplete result in the completion URL’s `metadata` parameter. If clients need to fetch the search result in a certain language, they’re responsible for specifying the `lang` parameter in the request.
- `displayLines` ([string]): A JSON string array to use to create a long form of display text for the completion result.
- `location` (Location): A [`Location`](location.md) object that specifies the location of the result in terms of its latitude and longitude.
- `structuredAddress` (StructuredAddress): A [`StructuredAddress`](structuredaddress.md) object that describes the detailed address components of a place.

## See Also

- [object DirectionsResponse](directionsresponse.md)
  An object that describes the directions from a starting location to a destination in terms routes, steps, and a series of waypoints.
- [object EtaResponse](etaresponse.md)
  An object that contains an array of one or more estimated times of arrival (ETAs).
- [object Location](location.md)
  An object that describes a location in terms of its longitude and latitude.
- [object MapRegion](mapregion.md)
  An object that describes a map region in terms of its upper-right and lower-left corners as a pair of geographic points.
- [object Place](place.md)
  An object that describes a place in terms of a variety of spatial, administrative, and qualitative properties.
- [object PlaceResults](placeresults.md)
  An object that contains an array of places.
- [object SearchAutocompleteResponse](searchautocompleteresponse.md)
  An array of autocomplete results.
- [object SearchMapRegion](searchmapregion.md)
  An object that describes an area to search in terms of its upper-right and lower-left corners as a pair of geographic points.
- [object SearchResponse](searchresponse.md)
  An object that contains the search region and an array of place descriptions that a search returns.
- [object StructuredAddress](structuredaddress.md)
  An object that describes the detailed address components of a place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult)*