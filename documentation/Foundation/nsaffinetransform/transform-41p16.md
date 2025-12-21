# transform(_:)

**Framework**: Foundation  
**Kind**: method

Applies the receiver’s transform to the specified point and returns the result.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func transform(_ aPoint: NSPoint) -> NSPoint
```

#### Return Value

The resulting point after applying the receiver’s transformations.

## Parameters

- `aPoint`: The point in the current coordinate system to which you want to apply the matrix.

## See Also

- [func transform(NSSize) -> NSSize](nsaffinetransform/transform(_:)-5r6ol.md)
  Applies the receiver’s transform to the specified size and returns the results.
- [func transform(NSBezierPath) -> NSBezierPath](nsaffinetransform/transform(_:)-6z1xo.md)
  Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-41p16)*