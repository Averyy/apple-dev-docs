# offsetBy(dx:dy:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a rectangle with an origin point that shifts by the specified amount.

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
func offsetBy(dx: Double, dy: Double) -> MKMapRect
```

```c
extern MKMapRect MKMapRectOffset(MKMapRect rect, double dx, double dy);
```

#### Return Value

The offset rectangle. If the original rectangle is `null`, that rectangle returns instead.

## Parameters

- `dx`: The amount (in map points) to shift the x-coordinate of the origin point.
- `dy`: The amount (in map points) to shift the x-coordinate of the origin point.

## See Also

### Modifying the rectangle
- [func union(MKMapRect) -> MKMapRect](./union%28_%29.md)
  Returns a rectangle that represents the union of two rectangles.
- [func intersection(MKMapRect) -> MKMapRect](./intersection%28_%29.md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func insetBy(dx: Double, dy: Double) -> MKMapRect](./insetby%28dx,dy%29.md)
  Returns the specified rectangle with an inset by the specified amounts.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](../mkmaprectdivide%28_,_,_,_,_%29.md)
  Divides the specified rectangle into two smaller rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/offsetby(dx:dy:))*