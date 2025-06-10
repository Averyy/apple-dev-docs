# pointCount

**Framework**: MapKit  
**Kind**: property

The number of points associated with the shape.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var pointCount: Int { get }
```

## See Also

- [func points() -> UnsafeMutablePointer<MKMapPoint>](mkmultipoint/points.md)
  Returns an array of map points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](mkmultipoint/location(atpointindex:).md)
  Translates a point index into a unit distance along the shape.
- [func locations(at: IndexSet) -> [CGFloat]](mkmultipoint/locations(at:).md)
  Translates a point index set into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/pointcount)*