# transform(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies an affine transform to this shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func transform(_ transform: CGAffineTransform) -> TransformedShape<Self>
```

#### Return Value

A transformed shape, based on its matrix values.

#### Discussion

Affine transforms present a mathematical approach to applying combinations of rotation, scaling, translation, and skew to shapes.

## Parameters

- `transform`: The affine transformation matrix to apply to this   shape.

## See Also

- [func trim(from: CGFloat, to: CGFloat) -> some Shape](shape/trim(from:to:).md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func size(CGSize) -> some Shape](shape/size(_:).md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(width: CGFloat, height: CGFloat) -> some Shape](shape/size(width:height:).md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func scale(CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](shape/scale(_:anchor:).md)
  Scales this shape without changing its bounding frame.
- [func scale(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](shape/scale(x:y:anchor:).md)
  Scales this shape without changing its bounding frame.
- [func rotation(Angle, anchor: UnitPoint) -> RotatedShape<Self>](shape/rotation(_:anchor:).md)
  Rotates this shape around an anchor point at the angle you specify.
- [func offset(_:)](shape/offset(_:).md)
  Changes the relative position of this shape using the specified point.
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](shape/offset(x:y:).md)
  Changes the relative position of this shape using the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/transform(_:))*