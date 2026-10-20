# intersection(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle that represents the intersection of two rectangles.

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
func intersection(_ rect2: MKMapRect) -> MKMapRect
```

```c
extern MKMapRect MKMapRectIntersection(MKMapRect rect1, MKMapRect rect2);
```

#### Return Value

The rectangle representing the intersection of the two rectangles, or [`null`](./null.md) if there’s no intersection.

## Parameters

- `rect2`: The second rectangle.

## See Also

### Modifying the rectangle
- [func union(MKMapRect) -> MKMapRect](./union%28_%29.md)
  Returns a rectangle that represents the union of two rectangles.
- [func insetBy(dx: Double, dy: Double) -> MKMapRect](./insetby%28dx,dy%29.md)
  Returns the specified rectangle with an inset by the specified amounts.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](./offsetby%28dx,dy%29.md)
  Returns a rectangle with an origin point that shifts by the specified amount.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](../mkmaprectdivide%28_,_,_,_,_%29.md)
  Divides the specified rectangle into two smaller rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/intersection(_:))*