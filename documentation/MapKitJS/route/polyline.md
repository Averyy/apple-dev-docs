# polyline

**Framework**: MapKit JS  
**Kind**: property

An instance of a polyline overlay that represents the path of a route.

**Availability**:
- MapKit JS 5.4+

## Declaration

```swift
attribute mapkit.PolylineOverlay polyline;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

You can add the value of the `polyline` property directly to the map.

```swift
var route = directions.route({
    origin: new mapkit.Coordinate(37.616934, -122.383790),
    destination: new mapkit.Coordinate(37.3349, -122.0090201)
}, function(error, data) {

    var polylines = data.routes.map(function(route) {
        return route.polyline;
    });

    map.showItems(polylines);

});
```

## See Also

- [path](route/path.md)
  An array of coordinate objects representing the path of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/polyline)*