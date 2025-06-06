# mapkit.MapSize

**Framework**: MapKit JS  
**Kind**: init

Creates an object containing the width and height of a projected coordinate span.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.MapSize(
	number width,
	number height
);
```

#### Discussion

The following example demonstrates how to create a `mapkit.MapSize` instance from map units:

```javascript
var mapSize = new mapkit.MapSize(0.3, 0.4);
var width = mapSize.width; // 0.3
var height = mapSize.height; // 0.4
```

## Parameters

- `width`: The distance in map units along the east-west axis of the map projection.
- `height`: The distance in map units along the north-south axis of the map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.mapsize/mapkit.mapsize)*