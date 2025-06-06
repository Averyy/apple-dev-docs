# init(x:y:width:height:)

**Framework**: MapKit  
**Kind**: init

Creates a new map rectangle structure from the specified values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(x: Double, y: Double, width: Double, height: Double)
```

#### Return Value

A map rectangle with the specified values.

## Parameters

- `x`: The point along the east-west axis of the map projection to use for the origin.
- `y`: The point along the north-south axis of the map projection to use for the origin.
- `width`: The width of the rectangle (measured using map points).
- `height`: The height of the rectangle (measured using map points).

## See Also

- [init()](mkmaprect/init.md)
  Creates the rectangle with an empty region.
- [init(origin: MKMapPoint, size: MKMapSize)](mkmaprect/init(origin:size:).md)
  Creates the map rectangle with the specified point and size.
- [init(MKMapRect)](mkcoordinateregion/init(_:).md)
  Returns the region that corresponds to the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/init(x:y:width:height:))*