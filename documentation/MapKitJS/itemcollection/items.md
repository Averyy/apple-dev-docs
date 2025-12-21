# items

**Framework**: MapKit JS  
**Kind**: property

A nested list of annotations, overlays, and other item collections.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get items(): Item[];
set items(items: Item | Item[] | null);
```

#### Discussion

Access the original GeoJSON data in the [`data`](itemcollection/data.md) object. To retrieve the data as MapKit JS items, use the [`items`](itemcollection/items.md) or [`getFlattenedItemList()`](itemcollection/getflatteneditemlist.md) objects.

## See Also

- [data](itemcollection/data.md)
  The raw GeoJSON data.
- [getFlattenedItemList()](itemcollection/getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/items)*