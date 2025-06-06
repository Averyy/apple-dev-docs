# location(atPointIndex:)

**Framework**: MapKit  
**Kind**: method

Translates a point index into a unit distance along the shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func location(atPointIndex index: Int) -> CGFloat
```

#### Return Value

A [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) value that indicates the unit distance along the shape.

## Parameters

- `index`: The index of the map point associated with the shape.

## See Also

- [func points() -> UnsafeMutablePointer<MKMapPoint>](mkmultipoint/points.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](mkmultipoint/pointcount.md)
  The number of points associated with the shape.
- [func locations(at: IndexSet) -> [CGFloat]](mkmultipoint/locations(at:).md)
  Translates a point index set into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/location(atpointindex:))*