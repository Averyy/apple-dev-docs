# autocompleteDidComplete

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate when the autocomplete request completes.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void autocompleteDidComplete(
	SearchAutocompleteResponse data
);
```

#### Discussion

MapKit JS calls this method on successful completion of an autocomplete request.

## Parameters

- `data`: The results from the search autocomplete request.

## See Also

- [autocompleteDidError](searchdelegate/autocompletediderror.md)
  Tells the delegate when the autocomplete request fails due to an error.
- [searchDidComplete](searchdelegate/searchdidcomplete.md)
  Tells the delegate when the search completes.
- [searchDidError](searchdelegate/searchdiderror.md)
  Tells the delegate when the search fails due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchdelegate/autocompletedidcomplete)*