# search(query, options)

**Framework**: MapKit JS  
**Kind**: method

Retrieves the results of a search query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
search(
    query: string | SearchAutocompleteResult,
    options?: SearchOptions,
): Promise<SearchResponse>;
```

#### Return Value

A promise that resolves with a [`SearchResponse`](searchresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

The [`search(query, options)`](search/search.md) method returns a set of locations that matches a user-entered query or a [`SearchAutocompleteResult`](searchautocompleteresult.md).

The resolved [`SearchResponse`](searchresponse.md) contains the following properties:

- [`places`](searchresponse/places.md) (array of [`Place`](place.md)). An array of [`Place`](place.md) objects. The places array is empty if there isn’t a match.
- [`query`](searchresponse/query.md) (String). The query that corresponds to the results, if you don’t use [`SearchAutocompleteResult`](searchautocompleteresult.md) to perform the search. Optional.
- [`boundingRegion`](searchresponse/boundingregion.md) ([`CoordinateRegion`](coordinateregion.md)). A region that encloses the search results. This property isn’t present if there aren’t any results.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](searchoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

The following example searches for *coffee shop* in and around the visible map area, and adds the results as annotations:

```javascript
const search = new mapkit.Search({ region: map.region });

try {
    const data = await search.search("coffee shop");
    const annotations = data.places.map((place) => {
        const annotation = new mapkit.MarkerAnnotation(place.coordinate);
        annotation.title = place.name;
        annotation.subtitle = place.formattedAddress;
        annotation.color = "#9B6134";
        return annotation;
    });
    map.showItems(annotations);
} catch (error) {
    // Handle the search error.
}
```

## Parameters

- `query`: A `String` or a [`SearchAutocompleteResult`](searchautocompleteresult.md).
- `options`: Options for this specific query that supersede values set on the [`Search`](search.md) object. See [`SearchOptions`](searchoptions.md).

## See Also

- [type SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [interface SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.
- [interface SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/search)*