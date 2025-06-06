# SearchAutocompleteResult

**Framework**: MapKit JS  
**Kind**: struct

The result of an autocomplete query, including display lines and a coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary SearchAutocompleteResult {
	string[] displayLines;
	mapkit.Coordinate coordinate;
};
```

#### Overview

You can use search and search autocomplete in sequence by passing a [`SearchAutocompleteResult`](searchautocompleteresult.md) object as the query parameter of a search. For example, you can present the display strings of a collection of search autocomplete results to the user while maintaining a mapping to the original [`SearchAutocompleteResult`](searchautocompleteresult.md) object. When the user selects a result, make a search request with the corresponding [`SearchAutocompleteResult`](searchautocompleteresult.md) object to retrieve more information about the place.

## Topics

### Autocomplete results
- [coordinate](searchautocompleteresult/coordinate.md)
  The coordinate of the result when it corresponds to a single place.
- [displayLines](searchautocompleteresult/displaylines.md)
  Lines of text to display to the user in an autocomplete menu.

## See Also

- [autocomplete](mapkit.search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteresult)*