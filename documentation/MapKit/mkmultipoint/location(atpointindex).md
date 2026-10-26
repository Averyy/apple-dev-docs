# location(atPointIndex:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Translates a point index into a unit distance along the shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func location(atPointIndex index: Int) -> CGFloat
```

```objc
- (CGFloat) locationAtPointIndex:(NSUInteger) index;
```

#### Return Value

A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value that indicates the unit distance along the shape.

## Parameters

- `index`: The index of the map point associated with the shape.

## See Also

### Accessing the points in the shape
- [func points() -> UnsafeMutablePointer<MKMapPoint>](./points%28%29.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](./pointcount.md)
  The number of points associated with the shape.
- [func locations(at: IndexSet) -> [CGFloat]](./locations%28at%29.md)
  Translates a point index set into a unit distance along the shape.
- [- locationsAtPointIndexes:](./locationsatpointindexes_.md)
  Returns a set of unit distance values that correspond to the point indexes along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/location(atpointindex:))*