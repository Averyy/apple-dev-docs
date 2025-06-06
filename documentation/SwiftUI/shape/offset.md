# offset(_:)

**Framework**: SwiftUI  
**Kind**: method

Changes the relative position of this shape using the specified point.

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
func offset(_ offset: CGPoint) -> OffsetShape<Self>
```

#### Return Value

A shape offset by the specified amount.

#### Discussion

The following example renders two circles. It places one circle at its default position. The second circle is outlined with a stroke, positioned on top of the first circle and offset by 100 points to the left and 50 points below.

```swift
Circle()
.overlay(
    Circle()
    .offset(CGPoint(x: -100, y: 50))
    .stroke()
)
```

## Parameters

- `offset`: The amount, in points, by which you offset the   shape. Negative numbers are to the left and up; positive numbers are   to the right and down.

## See Also

- [func trim(from: CGFloat, to: CGFloat) -> some Shape](shape/trim(from:to:).md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func transform(CGAffineTransform) -> TransformedShape<Self>](shape/transform(_:).md)
  Applies an affine transform to this shape.
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
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](shape/offset(x:y:).md)
  Changes the relative position of this shape using the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/offset(_:))*