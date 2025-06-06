# trim(from:to:)

**Framework**: SwiftUI  
**Kind**: method

Trims this shape by a fractional amount based on its representation as a path.

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
func trim(from startFraction: CGFloat = 0, to endFraction: CGFloat = 1) -> some Shape
```

#### Return Value

A shape built by capturing a portion of this shape’s path.

#### Discussion

To create a `Shape` instance, you define the shape’s path using lines and curves. Use the `trim(from:to:)` method to draw a portion of a shape by ignoring portions of the beginning and ending of the shape’s path.

For example, if you’re drawing a figure eight or infinity symbol (∞) starting from its center, setting the `startFraction` and `endFraction` to different values determines the parts of the overall shape.

The following example shows a simplified infinity symbol that draws only three quarters of the full shape. That is, of the two lobes of the symbol, one lobe is complete and the other is half complete.

```swift
Path { path in
    path.addLines([
        .init(x: 2, y: 1),
        .init(x: 1, y: 0),
        .init(x: 0, y: 1),
        .init(x: 1, y: 2),
        .init(x: 3, y: 0),
        .init(x: 4, y: 1),
        .init(x: 3, y: 2),
        .init(x: 2, y: 1)
    ])
}
.trim(from: 0.25, to: 1.0)
.scale(50, anchor: .topLeading)
.stroke(Color.black, lineWidth: 3)
```

Changing the parameters of `trim(from:to:)` to `.trim(from: 0, to: 1)` draws the full infinity symbol, while `.trim(from: 0, to: 0.5)` draws only the left lobe of the symbol.

## Parameters

- `startFraction`: The fraction of the way through drawing this shape   where drawing starts.
- `endFraction`: The fraction of the way through drawing this shape   where drawing ends.

## See Also

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
- [func offset(_:)](shape/offset(_:).md)
  Changes the relative position of this shape using the specified point.
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](shape/offset(x:y:).md)
  Changes the relative position of this shape using the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/trim(from:to:))*