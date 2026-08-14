# autocomplete(query, options)

**Framework**: MapKit JS  
**Kind**: method

Retrieves a list of autocomplete results for the specified search query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
autocomplete(
    query: string,
    options?: SearchAutocompleteOptions,
): Promise<SearchAutocompleteResponse>;
```

#### Return Value

A promise that resolves with a [`SearchAutocompleteResponse`](searchautocompleteresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

To provide the user with a menu of search suggestions, invoke the [`autocomplete()`](search/autocomplete.md) method as users type. This method minimizes typing and brings users the results they’re looking for.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](searchoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `query`: A string that represents the user’s search in progress.
- `options`: Options for this specific query that supersede values set on the [`Search`](search.md) object. See [`SearchAutocompleteOptions`](searchautocompleteoptions.md).

## See Also

- [interface SearchAutocompleteOptions](searchautocompleteoptions.md)
  Options you provide to constrain an autocomplete request.
- [interface SearchAutocompleteResponse](searchautocompleteresponse.md)
  An object containing the response from an autocomplete request.
- [class SearchAutocompleteResult](searchautocompleteresult.md)
  The result of an autocomplete query, including display lines and a coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/autocomplete)*