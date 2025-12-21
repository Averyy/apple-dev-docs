# new Search(options)

**Framework**: MapKit JS  
**Kind**: init

Creates a search object with optional initial values that you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(options?: SearchConstructorOptions);
```

#### Discussion

To use search, create an instance of a [`Search`](search.md). You can optionally set properties of the search object by providing a dictionary of [`SearchConstructorOptions`](searchconstructoroptions.md) on initialization.

```javascript
const search = new mapkit.Search({
    language: "en-GB",
    getsUserLocation: true,
    region: map.region
});
```

## See Also

- [interface SearchConstructorOptions](searchconstructoroptions.md)
  Options you provide when you create a search object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/searchconstructor)*