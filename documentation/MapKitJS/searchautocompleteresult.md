# SearchAutocompleteResult

**Framework**: MapKit JS  
**Kind**: class

The result of an autocomplete query, including display lines and a coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class SearchAutocompleteResult
```

#### Overview

You can use search and search autocomplete in sequence by passing a [`SearchAutocompleteResult`](searchautocompleteresult.md) object as the query parameter of a search. For example, you can present the display strings of a collection of search autocomplete results to the user while maintaining a mapping to the original [`SearchAutocompleteResult`](searchautocompleteresult.md) object. When the user selects a result, make a search request with the corresponding [`SearchAutocompleteResult`](searchautocompleteresult.md) object to retrieve more information about the place.

## Topics

### Autocomplete results
- [coordinate](searchautocompleteresult/coordinate.md)
  The coordinate of the result when it corresponds to a single place.
- [displayLines](searchautocompleteresult/displaylines.md)
  Lines of text to display to the user in an autocomplete menu.
### Instance Properties
- [administrativeArea](searchautocompleteresult/administrativearea.md)
  The name of the state or province of the place.
- [administrativeAreaCode](searchautocompleteresult/administrativeareacode.md)
  The official abbreviation for the state or area.
- [alternateIds](searchautocompleteresult/alternateids.md)
  A list of alternate Place IDs that identify a feature.
- [areasOfInterest](searchautocompleteresult/areasofinterest.md)
  An array of common names of the area in which the place resides.
- [dependentLocalities](searchautocompleteresult/dependentlocalities.md)
  An array of common names for the local area or neighborhood of the place.
- [fullThoroughfare](searchautocompleteresult/fullthoroughfare.md)
  A combination of the thoroughfare and subthoroughfare.
- [id](searchautocompleteresult/id.md)
  The Place ID that identifies a feature.
- [locality](searchautocompleteresult/locality.md)
  The city of the place.
- [name](searchautocompleteresult/name.md)
  The name of the place.
- [postCode](searchautocompleteresult/postcode.md)
  The postal code of the place.
- [subLocality](searchautocompleteresult/sublocality.md)
  The name of the area within the locality.
- [subThoroughfare](searchautocompleteresult/subthoroughfare.md)
  The street number at the place.
- [thoroughfare](searchautocompleteresult/thoroughfare.md)
  The street name at the place.

## See Also

- [autocomplete(query, callback, options)](search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [interface SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [interface SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteresult)*