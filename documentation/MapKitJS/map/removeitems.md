# removeItems(items)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Removes a collection of annotations, overlays, or other item collections from the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
removeItems(items: (Overlay | Annotation)[]): (Annotation | Overlay)[];
```

#### Return Value

Returns an array of items removed from the map.

#### Discussion

This method doesn’t change the map’s visible region. Use [`showItems()`](./showitems.md) with a list of items to focus on to update the map’s view.

## Parameters

- `items`: An array of annotations, overlays, or the data returned from [`importGeoJSON()`](../mapkit/importgeojson.md) to display on the map.

## See Also

### Adding and removing geographical features
- [addItems(items)](./additems.md)
  Adds a collection of annotations, overlays, or other item collections to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/removeitems)*