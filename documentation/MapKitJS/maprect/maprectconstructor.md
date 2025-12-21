# new MapRect(x, y, width, height)

**Framework**: MapKit JS  
**Kind**: init

Creates an object that represents a rectangular region of the map projection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(x?: number, y?: number, width?: number, height?: number);
```

#### Discussion

The following example demonstrates how to create a `mapkit.MapRect` instance from map units and inspect the object’s `origin` and `size` properties:

```javascript
// Defining a MapRect (x, y, width, height):
const mapRect = new mapkit.MapRect(0.1, 0.2, 0.3, 0.4);

// mapRect.origin is a MapPoint:
const x = mapRect.origin.x; // 0.1
const y = mapRect.origin.x; // 0.2

// mapRect.size is a MapSize:
const width = mapRect.size.width; // 0.3
const height = mapRect.size.height; // 0.4
```

## Parameters

- `x`: The origin point along the east-west axis of the map projection.
- `y`: The origin point along the north-south axis of the map projection.
- `width`: The distance, in map units, along the east-west axis of the map projection.
- `height`: The distance, in map units, along the north-south axis of the map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maprect/maprectconstructor)*