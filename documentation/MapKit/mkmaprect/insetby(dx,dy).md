# insetBy(dx:dy:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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

```c
extern MKMapRect MKMapRectInset(MKMapRect rect, double dx, double dy);
```

## Return Value

The inset rectangle. If the original rectangle was null, that rectangle is returned instead.

## Parameters

- `dx`: The amount (in map points) to subtract from both sides along the x-axis.
- `dy`: The amount (in map points) to subtract from both sides along the x-axis.

## See Also

### Modifying the rectangle
- [func union(MKMapRect) -> MKMapRect](./union%28_%29.md)
  Returns a rectangle that represents the union of two rectangles.
- [func intersection(MKMapRect) -> MKMapRect](./intersection%28_%29.md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](./offsetby%28dx,dy%29.md)
  Returns a rectangle with an origin point that shifts by the specified amount.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](../mkmaprectdivide%28_,_,_,_,_%29.md)
  Divides the specified rectangle into two smaller rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/insetby(dx:dy:))*