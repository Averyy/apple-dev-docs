# SearchAutocompleteResponse

**Framework**: MapKit JS  
**Kind**: struct

An object containing the response from an autocomplete request.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary SearchAutocompleteResponse {
	string query;
	SearchAutocompleteResult[] results;
};
```

## Topics

### Response
- [query](searchautocompleteresponse/query.md)
  The query string used to perform the autocomplete request.
- [results](searchautocompleteresponse/results.md)
  The results from an autocomplete request.

## See Also

- [autocomplete](mapkit.search/autocomplete.md)
  Retrieves a list of autocomplete results for the specified search query.
- [SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchautocompleteresponse)*