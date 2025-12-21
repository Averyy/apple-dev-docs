# transform(_:)

**Framework**: Foundation  
**Kind**: method

Applies the receiver’s transform to the specified size and returns the results.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func transform(_ aSize: NSSize) -> NSSize
```

#### Return Value

The resulting size after applying the receiver’s transformations.

#### Discussion

This method applies the current rotation and scaling factors to `aSize`; it does not apply translation factors. You can think of this method as transforming a vector whose origin is (0, 0) and whose end point is specified by the value in `aSize`. After the rotation and scaling factors are applied, this method effectively returns the end point of the new vector.

This method is useful for transforming delta or distance values when you need to take scaling and rotation factors into account.

## Parameters

- `aSize`: The size data to which you want to apply the matrix.

## See Also

- [func transform(NSPoint) -> NSPoint](nsaffinetransform/transform(_:)-41p16.md)
  Applies the receiver’s transform to the specified point and returns the result.
- [func transform(NSBezierPath) -> NSBezierPath](nsaffinetransform/transform(_:)-6z1xo.md)
  Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transform(_:)-5r6ol)*