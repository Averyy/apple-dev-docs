# insetBy(dx:dy:)

**Framework**: MapKit  
**Kind**: method

Returns the specified rectangle with an inset by the specified amounts.

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
func insetBy(dx: Double, dy: Double) -> MKMapRect
```

#### Return Value

The inset rectangle. If the original rectangle was null, that rectangle is returned instead.

## Parameters

- `dx`: The amount (in map points) to subtract from both sides along the x-axis.
- `dy`: The amount (in map points) to subtract from both sides along the x-axis.

## See Also

- [func union(MKMapRect) -> MKMapRect](mkmaprect/union(_:).md)
  Returns a rectangle that represents the union of two rectangles.
- [func intersection(MKMapRect) -> MKMapRect](mkmaprect/intersection(_:).md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/offsetby(dx:dy:).md)
  Returns a rectangle with an origin point that shifts by the specified amount.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](mkmaprectdivide(_:_:_:_:_:).md)
  Divides the specified rectangle into two smaller rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/insetby(dx:dy:))*