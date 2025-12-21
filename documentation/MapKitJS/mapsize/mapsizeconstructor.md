# new MapSize(width, height)

**Framework**: MapKit JS  
**Kind**: init

Creates an object containing the width and height of a projected coordinate span.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(width?: number, height?: number);
```

#### Discussion

The following example demonstrates how to create a `mapkit.MapSize` instance from map units:

```javascript
const mapSize = new mapkit.MapSize(0.3, 0.4);
const width = mapSize.width; // 0.3
const height = mapSize.height; // 0.4
```

## Parameters

- `width`: The distance in map units along the east-west axis of the map projection.
- `height`: The distance in map units along the north-south axis of the map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapsize/mapsizeconstructor)*