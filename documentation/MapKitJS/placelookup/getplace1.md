# getPlace(annotation, options)

**Framework**: MapKit JS  
**Kind**: method

Obtains the place associated with a map feature annotation.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
getPlace(
    annotation: MapFeatureAnnotation,
    options?: PlaceLookupOptions,
): Promise<Place>;
```

#### Return Value

A promise that resolves with a [`Place`](place.md) on success, or rejects with an `Error` on failure.

#### Discussion

Use this method to retrieve the full [`Place`](place.md) information for a [`MapFeatureAnnotation`](mapfeatureannotation.md) that a person selects on the map.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](placelookupoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the returned promise rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `annotation`: The [`MapFeatureAnnotation`](mapfeatureannotation.md) to look up.
- `options`: Options that can overwrite the same options set on the property or that you supplied to the [`PlaceLookup`](placelookup.md) constructor. See [`PlaceLookupOptions`](placelookupoptions.md).

## See Also

- [getPlace(id, options)](placelookup/getplace.md)
  Obtains a place using its identifier.
- [interface PlaceLookupOptions](placelookupoptions.md)
  Options for place lookup requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placelookup/getplace1)*