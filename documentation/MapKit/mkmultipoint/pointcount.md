# pointCount

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSUInteger pointCount;
```

## See Also

### Accessing the points in the shape
- [func points() -> UnsafeMutablePointer<MKMapPoint>](./points%28%29.md)
  Returns an array of map points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](./location%28atpointindex%29.md)
  Translates a point index into a unit distance along the shape.
- [func locations(at: IndexSet) -> [CGFloat]](./locations%28at%29.md)
  Translates a point index set into a unit distance along the shape.
- [- locationsAtPointIndexes:](./locationsatpointindexes_.md)
  Returns a set of unit distance values that correspond to the point indexes along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/pointcount)*