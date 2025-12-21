# itemForGeometryCollection(item, object)

**Framework**: MapKit JS  
**Kind**: method

Overrides a geometry collection with the provided item and object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForGeometryCollection?<D extends GeoJSONTypes.GeometryCollection>(
        item: ItemCollection<D>,
        object: D,
    ): ItemCollection<D> | Item[] | null;
```

#### Return Value

A map item for the geometry collection.

## Parameters

- `item`: An item the system creates for the geometry of the geometry collection.
- `object`: The original GeoJSON object for the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforgeometrycollection)*