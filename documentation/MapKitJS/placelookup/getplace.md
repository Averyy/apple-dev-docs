# getPlace(id, options)

**Framework**: MapKit JS  
**Kind**: method

Obtains a place using its identifier.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
getPlace(id: string, options?: PlaceLookupOptions): Promise<Place>;
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Return Value

A promise that resolves with a [`Place`](place.md) on success, or rejects with an `Error` on failure.

#### Discussion

For information about Places, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids).

Pass an `AbortSignal` from an `AbortController` to the [`signal`](placelookupoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `id`: The Place ID that refers to the [`Place`](place.md) object to fetch.
- `options`: Options that can overwrite the same options set on the property or that you supplied to the [`PlaceLookup`](placelookup.md) constructor. See [`PlaceLookupOptions`](placelookupoptions.md).

## See Also

- [getPlace(annotation, options)](placelookup/getplace1.md)
  Obtains the place associated with a map feature annotation.
- [interface PlaceLookupOptions](placelookupoptions.md)
  Options for place lookup requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placelookup/getplace)*