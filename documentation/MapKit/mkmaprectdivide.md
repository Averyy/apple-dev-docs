# MKMapRectDivide(_:_:_:_:_:)

**Framework**: MapKit  
**Kind**: func

Divides the specified rectangle into two smaller rectangles.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func MKMapRectDivide(_ rect: MKMapRect, _ slice: UnsafeMutablePointer<MKMapRect>, _ remainder: UnsafeMutablePointer<MKMapRect>, _ amount: Double, _ edge: CGRectEdge)
```

## Parameters

- `rect`: The rectangle to divide.
- `slice`: On input, a pointer to a map rectangle. On output, this parameter contains the portion of   that the method removes.
- `remainder`: On input, a pointer to a map rectangle. On output, this parameter contains the remaining portion of   that the method doesn’t remove.
- `amount`: The amount of   to remove along the specified edge. If this value is negative, the system sets it to  .
- `edge`: The edge from which to remove the specified amount.

## See Also

- [func union(MKMapRect) -> MKMapRect](mkmaprect/union(_:).md)
  Returns a rectangle that represents the union of two rectangles.
- [func intersection(MKMapRect) -> MKMapRect](mkmaprect/intersection(_:).md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func insetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/insetby(dx:dy:).md)
  Returns the specified rectangle with an inset by the specified amounts.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/offsetby(dx:dy:).md)
  Returns a rectangle with an origin point that shifts by the specified amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprectdivide(_:_:_:_:_:))*