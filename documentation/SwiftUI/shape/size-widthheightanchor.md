# size(width:height:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func size(width: CGFloat, height: CGFloat, anchor: UnitPoint) -> some Shape
```

#### Return Value

A new shape constrained to the given `size`, and positioned using `anchor`.

#### Discussion

The `anchor` parameter determines how the shape will be positioned within the container when the path’s bounds and the container’s bounds are not equal. This does not affect the layout properties of any views created from the shape (e.g. by filling it).

## Parameters

- `width`: The width to constrain the shape to.
- `height`: The height to constrain the shape to.
- `anchor`: The anchor to use to determine how to position the new shape.

## See Also

- [func trim(from: CGFloat, to: CGFloat) -> some Shape](shape/trim(from:to:).md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func transform(CGAffineTransform) -> TransformedShape<Self>](shape/transform(_:).md)
  Applies an affine transform to this shape.
- [func size(CGSize) -> some Shape](shape/size(_:).md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(CGSize, anchor: UnitPoint) -> some Shape](shape/size(_:anchor:).md)
  Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/size(width:height:anchor:))*