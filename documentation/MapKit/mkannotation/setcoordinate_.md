# setCoordinate:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the new center point of the annotation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) setCoordinate:(CLLocationCoordinate2D) newCoordinate;
```

## Discussion

Annotations that support dragging should implement this method to update the position of the annotation.

If you implement this method, you must update the value of the coordinate in a key-value observing (KVO) compliant way. For more information on how to implement support for KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Parameters

- `newCoordinate`: The new center point for the annotation.

## See Also

### Position attributes
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The center point (specified as a map coordinate) of the annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotation/setcoordinate:)*