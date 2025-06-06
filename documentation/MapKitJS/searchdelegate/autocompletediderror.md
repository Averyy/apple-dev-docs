# autocompleteDidError

**Framework**: MapKit JS  
**Kind**: method

Tells the delegate when the autocomplete request fails due to an error.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void autocompleteDidError(
	Error error
);
```

#### Discussion

MapKit JS calls this method when an autocomplete request fails.

## Parameters

- `error`: The error from a failed autocomplete request.

## See Also

- [autocompleteDidComplete](searchdelegate/autocompletedidcomplete.md)
  Tells the delegate when the autocomplete request completes.
- [searchDidComplete](searchdelegate/searchdidcomplete.md)
  Tells the delegate when the search completes.
- [searchDidError](searchdelegate/searchdiderror.md)
  Tells the delegate when the search fails due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchdelegate/autocompletediderror)*