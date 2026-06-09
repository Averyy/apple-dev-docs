# getPlace(id, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Obtains a place using its identifier.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
getPlace(
    id: string,
    callback: (error: Error | null, result: Place | null) => void,
    options?: PlaceLookupOptions,
): Promise<Place>;
```

#### Return Value

A promise that resolves with a [`Place`](place.md) on success.

#### Discussion

For information about Places, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids).

## Parameters

- `id`: The Place ID that refers to the [`Place`](place.md) object to fetch.
- `callback`: A callback function that is invoked with `error` and `data` parameters.
- `options`: Options that can overwrite the same options set on the property or that you supplied to the [`PlaceLookup`](placelookup.md) constructor. See [`PlaceLookupOptions`](placelookupoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placelookup/getplace2)*