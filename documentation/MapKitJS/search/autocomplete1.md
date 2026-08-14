# autocomplete(query, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Retrieves a list of autocomplete results for the specified search query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
autocomplete(
    query: string,
    callback: SearchDelegate<SearchAutocompleteResponse>,
    options?: SearchAutocompleteOptions,
): Promise<SearchAutocompleteResponse>;
```

#### Return Value

A promise that resolves when the autocomplete request completes.

#### Discussion

To provide the user with a menu of search suggestions, invoke the [`autocomplete()`](search/autocomplete1.md) method as users type. This method minimizes typing and brings users the results they’re looking for.

MapKit JS invokes the `callback` function on failure and success with two arguments, `error` and `data`:

- `error`. An error object that contains an error code and descriptive message.
- `data`. A [`SearchAutocompleteResponse`](searchautocompleteresponse.md) object.

The system doesn’t call the callback function or delegate if you cancel the request before MapKit JS receives a response.

## Parameters

- `query`: A string that represents the user’s search in progress.
- `callback`: A callback function or delegate object.
- `options`: With the [`SearchAutocompleteOptions`](searchautocompleteoptions.md) hash, you have the option to constrain the search to a desired area using the [`coordinate`](searchconstructoroptions/coordinate.md) or [`region`](searchconstructoroptions/region.md) properties. A coordinate or region you supply here overrides the same property you supply to the [`Search`](search.md) constructor. You also have the option to override the [`language`](service/language.md) for the search constructor. For example, `{ "language: "fr-CA" }` tells the server to send results localized to Canadian French. For a complete list of options you can use to constrain your search, see [`SearchAutocompleteOptions`](searchautocompleteoptions.md).

## See Also

- [cancel(promise)](service/cancel.md)
  Cancels a request using the provided request promise.
- [RegionPriority](search/regionpriority-data.var.md)
  A static property that allows you to access region priority enumeration.
- [search(query, callback, options)](search/search1.md)
  Retrieves the results of a search query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/autocomplete1)*