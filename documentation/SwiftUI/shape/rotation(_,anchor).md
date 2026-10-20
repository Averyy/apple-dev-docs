# rotation(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Rotates this shape around an anchor point at the angle you specify.

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
nonisolated
func rotation(_ angle: Angle, anchor: UnitPoint = .center) -> RotatedShape<Self>
```

#### Return Value

A rotated shape.

#### Discussion

The following example rotates a square by 45 degrees to the right to create a diamond shape:

```swift
RoundedRectangle(cornerRadius: 10)
.rotation(Angle(degrees: 45))
.aspectRatio(1.0, contentMode: .fit)
```

## Parameters

- `angle`: The angle of rotation to apply. Positive angles rotate clockwise; negative angles rotate counterclockwise.
- `anchor`: The point to rotate the shape around.

## See Also

### Transforming a shape
- [func trim(from: CGFloat, to: CGFloat) -> some Shape](./trim%28from,to%29.md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func transform(CGAffineTransform) -> TransformedShape<Self>](./transform%28_%29.md)
  Applies an affine transform to this shape.
- [func size(CGSize) -> some Shape](./size%28_%29.md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(CGSize, anchor: UnitPoint) -> some Shape](./size%28_,anchor%29.md)
  Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [func size(width: CGFloat, height: CGFloat) -> some Shape](./size%28width,height%29.md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(width: CGFloat, height: CGFloat, anchor: UnitPoint) -> some Shape](./size%28width,height,anchor%29.md)
  Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [func scale(CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](./scale%28_,anchor%29.md)
  Scales this shape without changing its bounding frame.
- [func scale(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](./scale%28x,y,anchor%29.md)
  Scales this shape without changing its bounding frame.
- [func offset(_:)](./offset%28_%29.md)
  Changes the relative position of this shape using the specified point.
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](./offset%28x,y%29.md)
  Changes the relative position of this shape using the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rotation(_:anchor:))*