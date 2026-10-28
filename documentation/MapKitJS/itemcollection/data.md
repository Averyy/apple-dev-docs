# data

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The raw GeoJSON data.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get data(): D | null;
set data(data: D | null);
```

## Discussion

Use the [`data`](./data.md) object to view the original GeoJSON data. To retrieve the data as MapKit JS items, use the [`items`](./items.md) or [`getFlattenedItemList()`](./getflatteneditemlist.md) objects.

## See Also

### Item collection properties
- [getFlattenedItemList()](./getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.
- [items](./items.md)
  A nested list of annotations, overlays, and other item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/data)*