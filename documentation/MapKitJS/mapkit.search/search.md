# search

**Framework**: MapKit JS  
**Kind**: method

Retrieves the results of a search query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
number search(
	string|SearchAutocompleteResult query,
	function|SearchDelegate callback,
	optional SearchOptions options
);
```

#### Return Value

This method returns a request ID (integer) that you can pass to [`cancel`](mapkit.search/cancel.md) to stop a pending request.

#### Discussion

The [`search`](mapkit.search/search.md) method returns a set of locations that matches a user-entered query or a [`SearchAutocompleteResult`](searchautocompleteresult.md).

MapKit JS invokes the `callback` function on failure and success with two arguments, `error` and `data`. If you cancel the request before you receive a response, the system doesn’t call this function. The callback can also be a delegate object.

The arguments are:

- `error` (Error). An error code and descriptive message.
- `data` (Object). An object the system parses from a server-returned JSON response. This object contains `query`, `displayRegion`, and `places` properties.

`The data` properties include:

- `query` (String). The query corresponding to the results, if you don’t use [`SearchAutocompleteResult`](searchautocompleteresult.md) to perform the search. Optional.
- `displayRegion` ([`mapkit.CoordinateRegion`](mapkit.coordinateregion/mapkit.coordinateregion.md)). A region that encloses the search results. This property isn’t present if there aren’t any results.
- `places` (Array of [`Place`](place.md)). An array of [`Place`](place.md) objects. The places array is empty if there isn’t a match.

The following example searches for  in and around the visible map area, and adds the results as annotations:

```javascript
var search = new mapkit.Search({ region: map.region });

search.search("coffee shop", function(error, data) {
    if (error) {
        // Handle the search error.
        return;
    }
    var annotations = data.places.map(function(place) {
        var annotation = new mapkit.MarkerAnnotation(place.coordinate);
        annotation.title = place.name;
        annotation.subtitle = place.formattedAddress;
        annotation.color = "#9B6134";
        return annotation;
    });
    map.showItems(annotations);
});
```

## Parameters

- `query`: A   or a  .
- `callback`: A callback function or delegate object.
- `options`: With the   hash, you can constrain the search to a desired area using the   or   properties. A coordinate or region you supply here overrides the same property you supply to the   constructor. Another option is  . For example, {  ’ } tells the server to send results localized to Canadian French. If you set it, this option overrides the language the system provides to the search constructor.

## See Also

- [SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.
- [SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.search/search)*