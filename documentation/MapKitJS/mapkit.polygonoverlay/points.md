# points

**Framework**: MapKit JS  
**Kind**: property

One or more arrays of coordinates that define the polygon overlay shape.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Coordinate[] points;
```

#### Discussion

MapKit JS represents the points in the polygon as an array of arrays of coordinates, or an array of coordinates. (For the latter, MapKit JS autowraps the array with an enclosing array). When reading this property, an array of arrays of coordinates always returns. This is an array of arrays because complex polygons can form from multiple polygons, with each array containing the points of a polygon. MapKit JS determines  of the aggregate polygon by the `fillRule` property in this object’s `style` property.

A copy of the overlay’s array returns on read, so changing the array’s elements has no effect on the overlay. To change the overlay’s points, assign a new array. MapKit JS doesn’t draw an array of points with fewer than three elements on the map.

The following example creates a rectangle overlay with two triangles cut out of it:

```swift
// Creates an array of coordinates.
function toCoordinates(array) {
    return array.map(function(element) {
        return new mapkit.Coordinate(element[0], element[1]);
    });
}

var rectangle = [ [0, 0], [20, 0], [20, 10], [0, 10] ],
    triangle1 = [ [4, 4], [8, 4], [6, 6] ],
    triangle2 = [ [14, 4], [18, 4], [16, 6] ];

var points = [
    toCoordinates(rectangle),
    toCoordinates(triangle1),
    toCoordinates(triangle2)
];
var style = new mapkit.Style({
    strokeColor: "#777",
    fillRule: "evenodd"
});
var overlay = new mapkit.PolygonOverlay(points, { style: style });
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.polygonoverlay/points)*