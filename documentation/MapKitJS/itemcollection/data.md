# data

**Framework**: MapKit JS  
**Kind**: property

The raw GeoJSON data.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get data(): D | undefined;
set data(data: D | undefined);
```

#### Discussion

Use the [`data`](itemcollection/data.md) object to view the original GeoJSON data. To retrieve the data as MapKit JS items, use the [`items`](itemcollection/items.md) or [`getFlattenedItemList()`](itemcollection/getflatteneditemlist.md) objects.

## See Also

- [getFlattenedItemList()](itemcollection/getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.
- [items](itemcollection/items.md)
  A nested list of annotations, overlays, and other item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/data)*