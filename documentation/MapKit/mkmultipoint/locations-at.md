# locations(at:)

**Framework**: MapKit  
**Kind**: method

Translates a point index set into a unit distance along the shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func locations(at indexes: IndexSet) -> [CGFloat]
```

#### Return Value

An array of [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values.

## Parameters

- `indexes`: The index set of map points associated with the shape.

## See Also

- [func points() -> UnsafeMutablePointer<MKMapPoint>](mkmultipoint/points.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](mkmultipoint/pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](mkmultipoint/location(atpointindex:).md)
  Translates a point index into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/locations(at:))*