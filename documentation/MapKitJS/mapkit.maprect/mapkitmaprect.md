# mapkit.MapRect

**Framework**: MapKit JS  
**Kind**: init

Creates an object that represents a rectangular region of the map projection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.MapRect(
	number x,
	number y,
	number width,
	number height
);
```

#### Discussion

The following example demonstrates how to create a `mapkit.MapRect` instance from map units and inspect the object’s `origin` and `size` properties:

```javascript
// Defining a MapRect (x, y, width, height):
var mapRect = new mapkit.MapRect(0.1, 0.2, 0.3, 0.4);

// mapRect.origin is a MapPoint:
var x = mapRect.origin.x; // 0.1
var y = mapRect.origin.x; // 0.2

// mapRect.size is a MapSize:
var width = mapRect.size.width; // 0.3
var height = mapRect.size.height; // 0.4
```

## Parameters

- `x`: The origin point along the east-west axis of the map projection.
- `y`: The origin point along the north-south axis of the map projection.
- `width`: The distance, in map units, along the east-west axis of the map projection.
- `height`: The distance, in map units, along the north-south axis of the map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.maprect/mapkit.maprect)*