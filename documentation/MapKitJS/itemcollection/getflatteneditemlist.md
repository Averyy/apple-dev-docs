# getFlattenedItemList()

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

A flattened array of items that includes annotations and overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
getFlattenedItemList(): (Annotation | Overlay)[];
```

#### Discussion

The items in an [`ItemCollection`](../itemcollection.md) may include nested item collections. Use [`getFlattenedItemList()`](./getflatteneditemlist.md) when you need a flat array that contains individual annotations and overlays.

Access the original GeoJSON data in the [`data`](./data.md) object. To retrieve the data as MapKit JS items, use the [`items`](./items.md) or [`getFlattenedItemList()`](./getflatteneditemlist.md) objects.

## See Also

### Item collection properties
- [data](./data.md)
  The raw GeoJSON data.
- [items](./items.md)
  A nested list of annotations, overlays, and other item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/getflatteneditemlist)*