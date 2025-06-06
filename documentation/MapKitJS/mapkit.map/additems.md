# addItems

**Framework**: MapKit JS  
**Kind**: method

Adds a collection of annotations, overlays, or other item collections to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
(mapkit.Annotation|mapkit.Overlay|ItemCollection)[]|ItemCollection addItems();
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns an array of items added to the map.

#### Discussion

Use [`addItems`](mapkit.map/additems.md) to add elements to the map after importing them from [`importGeoJSON`](mapkit/importgeojson.md).

This method doesn’t change the map’s visible region. Use [`showItems`](mapkit.map/showitems.md) with the list of items to change the map’s view.

## Parameters

- `items`: An array of annotations, overlays, or the data returned from   to display on the map.

## See Also

- [removeItems](mapkit.map/removeitems.md)
  Removes a collection of annotations, overlays, or other item collections from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/additems)*