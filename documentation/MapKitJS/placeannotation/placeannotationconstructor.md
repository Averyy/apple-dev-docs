# new PlaceAnnotation(coordinate, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a new place annotation.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
constructor(
        coordinate: Coordinate | Place | SearchAutocompleteResult,
        options?: MarkerAnnotationConstructorOptions,
    );
```

#### Discussion

You’re required to provide a [`Place`](place.md) object, either by passing it as the first argument or setting [`place`](annotationconstructoroptions/place.md). If you don’t provide the required object, the call throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placeannotation/placeannotationconstructor)*