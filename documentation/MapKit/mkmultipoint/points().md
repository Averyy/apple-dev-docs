# points()

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of map points associated with the shape.

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
func points() -> UnsafeMutablePointer<MKMapPoint>
```

```objc
- (MKMapPoint *) points;
```

#### Return Value

An unsafe mutable array of [`MKMapPoint`](../mkmappoint.md) structures.

#### Discussion

The [`pointCount`](./pointcount.md) property specifies the number of points in the array.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Accessing the points in the shape
- [var pointCount: Int](./pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](./location%28atpointindex%29.md)
  Translates a point index into a unit distance along the shape.
- [func locations(at: IndexSet) -> [CGFloat]](./locations%28at%29.md)
  Translates a point index set into a unit distance along the shape.
- [- locationsAtPointIndexes:](./locationsatpointindexes_.md)
  Returns a set of unit distance values that correspond to the point indexes along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/points())*