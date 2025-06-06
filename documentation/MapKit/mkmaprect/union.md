# union(_:)

**Framework**: MapKit  
**Kind**: method

Returns a rectangle that represents the union of two rectangles.

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
func union(_ rect2: MKMapRect) -> MKMapRect
```

#### Return Value

A rectangle with an area that encompasses the two rectangles and the space between them.

#### Discussion

If either rectangle is `null`, this method returns the other rectangle. This method sets the origin point of the returned rectangle to the smaller of the x and y values for the two rectangles. Similarly, the method computes the size and width of the rectangle by taking the maximum x and y values and subtracting the x and y values for the new origin point.

## Parameters

- `rect2`: The second rectangle.

## See Also

- [func intersection(MKMapRect) -> MKMapRect](mkmaprect/intersection(_:).md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func insetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/insetby(dx:dy:).md)
  Returns the specified rectangle with an inset by the specified amounts.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/offsetby(dx:dy:).md)
  Returns a rectangle with an origin point that shifts by the specified amount.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](mkmaprectdivide(_:_:_:_:_:).md)
  Divides the specified rectangle into two smaller rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/union(_:))*