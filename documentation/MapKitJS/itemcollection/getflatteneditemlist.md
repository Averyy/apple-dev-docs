# getFlattenedItemList

**Framework**: MapKit JS  
**Kind**: property

A flattened array of items that includes annotations and overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute (mapkit.Annotation|mapkit.Overlay)[] getFlattenedItemList;
```

#### Discussion

The items in an [`ItemCollection`](itemcollection.md) may include nested item collections. Use [`getFlattenedItemList`](itemcollection/getflatteneditemlist.md) when you need a flat array that contains individual annotations and overlays.

Access the original GeoJSON data in the [`data`](itemcollection/data.md) object. To retrieve the data as MapKit JS items, use the [`items`](itemcollection/items.md) or [`getFlattenedItemList`](itemcollection/getflatteneditemlist.md) objects.

## See Also

- [data](itemcollection/data.md)
  The raw GeoJSON data.
- [items](itemcollection/items.md)
  A nested list of annotations, overlays, and other item collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection/getflatteneditemlist)*