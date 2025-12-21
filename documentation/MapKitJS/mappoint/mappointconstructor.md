# new MapPoint(x, y)

**Framework**: MapKit JS  
**Kind**: init

Creates a map location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(x?: number, y?: number);
```

#### Discussion

The x and y values of the point are unit values. MapKit JS expects the value to be between `0` and `1,` and represents an interpolated location on the map projection in the x and y coordinates, respectively.

The following example creates a point that’s one-tenth across the map projection along the x-axis, and half way across the y-axis:

```javascript
const mapPoint = new mapkit.MapPoint(0.1, 0.5);
const x = mapPoint.x; // 0.1
const y = mapPoint.y; // 0.5
```

## Parameters

- `x`: The point along the east-west axis of the map projection.
- `y`: The point along the north-south axis of the map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mappoint/mappointconstructor)*