# locationsAtPointIndexes:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a set of unit distance values that correspond to the point indexes along the shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSArray<NSNumber *> *) locationsAtPointIndexes:(NSIndexSet *) indexes;
```

## Return Value

An [`NSIndexSet`](../../Foundation/nsindexset.md) that corresponds to the point indexes along the shape.

## Parameters

- `indexes`: A set of map point indexes associated with the shape.

## See Also

### Accessing the points in the shape
- [func points() -> UnsafeMutablePointer<MKMapPoint>](./points%28%29.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](./pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](./location%28atpointindex%29.md)
  Translates a point index into a unit distance along the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/locationsatpointindexes:)*