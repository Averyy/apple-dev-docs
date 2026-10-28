# new MapSize(width, height)

**Framework**: MapKit JS  
**Kind**: init  
**Role**: Constructor

Creates an object containing the width and height of a projected coordinate span.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
constructor(width?: number, height?: number);
```

## Discussion

The following example demonstrates how to create a `mapkit.MapSize` instance from map units:

```javascript
const mapSize = new mapkit.MapSize(0.3, 0.4);
const width = mapSize.width; // 0.3
const height = mapSize.height; // 0.4
```

## Parameters

- `width`: The distance in map units along the east-west axis of the map projection.
- `height`: The distance in map units along the north-south axis of the map projection.

## See Also

### Creating a map size
- [interface MapSizeData](../mapsizedata.md)
  A plain object representation of dimensions in map units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapsize/mapsizeconstructor)*