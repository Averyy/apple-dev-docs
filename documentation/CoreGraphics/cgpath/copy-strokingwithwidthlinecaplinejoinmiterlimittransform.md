# copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)

**Framework**: Core Graphics  
**Kind**: method

Returns a new path equivalent to the results of drawing the path with a solid stroke.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy(strokingWithWidth lineWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform = .identity) -> CGPath
```

#### Return Value

A new path.

#### Discussion

The new path is created so that filling the new path draws the same pixels as stroking the original path with the specified line style.

## Parameters

- `lineWidth`: The line width to use, in user space units. The value must be greater than  .
- `lineCap`: The line cap style to render. (For equivalent   drawing methods, the default style is  .)
- `lineJoin`: The line join style to render. (For equivalent   drawing methods, the default style is  .)
- `miterLimit`: A value that limits how sharp individual corners in the path can be when using the   line join style. When the ratio of a the length required for a mitered corner to the line width exceeds this value, that corner uses the   style instead.
- `transform`: An affine transform to apply to the path before dashing. Defaults to the   transform if not specified.

## See Also

- [func copy() -> CGPath?](cgpath/copy.md)
  Creates an immutable copy of a graphics path.
- [func copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](cgpath/copy(using:).md)
  Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [func copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](cgpath/copy(dashingwithphase:lengths:transform:).md)
  Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [func mutableCopy() -> CGMutablePath?](cgpath/mutablecopy.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](cgpath/mutablecopy(using:).md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/copy(strokingwithwidth:linecap:linejoin:miterlimit:transform:))*