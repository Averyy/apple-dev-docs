# items

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A nested list of annotations, overlays, and other item collections.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get items(): Item[];
set items(items: Item | Item[] | null);
```

#### Discussion

Access the original GeoJSON data in the [`data`](./data.md) object. To retrieve the data as MapKit JS items, use the [`items`](./items.md) or [`getFlattenedItemList()`](./getflatteneditemlist.md) objects.

## See Also

### Item collection properties
- [data](./data.md)
  The raw GeoJSON data.
- [getFlattenedItemList()](./getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/items)*