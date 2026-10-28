# signal

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```
signal?: AbortSignal;
```

## Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending search or autocomplete request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

```javascript
const controller = new AbortController();
const search = new mapkit.Search();

try {
    const data = await search.search("coffee", { signal: controller.signal });
    // Handle results.
} catch (error) {
    if (error.name === "AbortError") {
        // The request was canceled.
    }
}

// Cancel the request at any time:
controller.abort();
```

## See Also

### Search options
- [addressFilter](./addressfilter.md)
  An address filter that lists which address components to include or exclude in search results.
- [coordinate](./coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [includeAddresses](./includeaddresses.md)
  A Boolean value that indicates whether the search results should include addresses.
- [includePhysicalFeatures](./includephysicalfeatures.md)
  A Boolean value that indicates whether the search results include physical features, such as mountain ranges, rivers, and ocean basins.
- [includePointsOfInterest](./includepointsofinterest.md)
  A Boolean value that indicates whether the search results should include points of interest.
- [language](./language.md)
  A language ID that determines the language for the search result text.
- [limitToCountries](./limittocountries.md)
  A string that constrains search results to within the provided countries.
- [pointOfInterestFilter](./pointofinterestfilter.md)
  A filter for including or excluding point-of-interest categories in search results.
- [region](./region.md)
  A map region that provides a hint for the geographic area to search.
- [regionPriority](./regionpriority.md)
  A region priority value that controls whether results occur outside, or strictly within, the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchoptions/signal)*