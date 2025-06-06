# searchDidComplete

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate when the search completes.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void searchDidComplete(
	SearchResponse data
);
```

#### Discussion

MapKit JS calls this method on successful completion of a [`search`](mapkit.search/search.md) request.

## Parameters

- `data`: The search results.

## See Also

- [autocompleteDidComplete](searchdelegate/autocompletedidcomplete.md)
  Tells the delegate when the autocomplete request completes.
- [autocompleteDidError](searchdelegate/autocompletediderror.md)
  Tells the delegate when the autocomplete request fails due to an error.
- [searchDidError](searchdelegate/searchdiderror.md)
  Tells the delegate when the search fails due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchdelegate/searchdidcomplete)*