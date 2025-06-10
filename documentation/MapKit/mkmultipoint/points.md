# points()

**Framework**: MapKit  
**Kind**: method

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

#### Return Value

An unsafe mutable array of [`MKMapPoint`](mkmappoint.md) structures.

#### Discussion

The [`pointCount`](mkmultipoint/pointcount.md) property specifies the number of points in the array.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [var pointCount: Int](mkmultipoint/pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](mkmultipoint/location(atpointindex:).md)
  Translates a point index into a unit distance along the shape.
- [func locations(at: IndexSet) -> [CGFloat]](mkmultipoint/locations(at:).md)
  Translates a point index set into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/points())*