# mapkit.Search

**Framework**: MapKit JS  
**Kind**: init

Creates a search object with optional initial values that you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Search(
	optional SearchConstructorOptions options
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

To use search, create an instance of a [`mapkit.Search`](mapkit.search/mapkit.search.md). You can optionally set properties of the search object by providing a dictionary of [`SearchConstructorOptions`](searchconstructoroptions.md) on initialization.

```javascript
var search = new mapkit.Search({
    language: "en-GB",
    getsUserLocation: true,
    region: map.region
});
```

## See Also

- [SearchConstructorOptions](searchconstructoroptions.md)
  Options you provide when you create a search object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.search/mapkit.search)*