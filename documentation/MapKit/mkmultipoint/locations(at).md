# locations(at:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Translates a point index set into a unit distance along the shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func locations(at indexes: IndexSet) -> [CGFloat]
```

## Return Value

An array of [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) values.

## Parameters

- `indexes`: The index set of map points associated with the shape.

## See Also

### Accessing the points in the shape
- [func points() -> UnsafeMutablePointer<MKMapPoint>](./points%28%29.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](./pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](./location%28atpointindex%29.md)
  Translates a point index into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/locations(at:))*