# searchDidError

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate when the search fails due to an error.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void searchDidError(
	Error error
);
```

#### Discussion

MapKit JS calls this method when the [`search`](mapkit.search/search.md) request fails.

## Parameters

- `error`: The error from a failed search.

## See Also

- [autocompleteDidComplete](searchdelegate/autocompletedidcomplete.md)
  Tells the delegate when the autocomplete request completes.
- [autocompleteDidError](searchdelegate/autocompletediderror.md)
  Tells the delegate when the autocomplete request fails due to an error.
- [searchDidComplete](searchdelegate/searchdidcomplete.md)
  Tells the delegate when the search completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchdelegate/searchdiderror)*