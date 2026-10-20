# addItems(items)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Adds a collection of annotations, overlays, or other item collections to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
addItems(items: (Overlay | Annotation)[]): (Annotation | Overlay)[];
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Return Value

Returns an array of items added to the map.

#### Discussion

Use [`addItems()`](./additems.md) to add elements to the map after importing them from [`importGeoJSON()`](../mapkit/importgeojson.md).

This method doesn’t change the map’s visible region. Use [`showItems()`](./showitems.md) with the list of items to change the map’s view.

## Parameters

- `items`: An array of annotations, overlays, or the data returned from [`importGeoJSON()`](../mapkit/importgeojson.md) to display on the map.

## See Also

### Adding and removing geographical features
- [removeItems(items)](./removeitems.md)
  Removes a collection of annotations, overlays, or other item collections from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/additems)*