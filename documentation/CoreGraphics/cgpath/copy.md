# copy()

**Framework**: Core Graphics  
**Kind**: method

Creates an immutable copy of a graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy() -> CGPath?
```

#### Return Value

A new, immutable copy of the specified path. You are responsible for releasing this object.

## See Also

- [func copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](cgpath/copy(using:).md)
  Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [func copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](cgpath/copy(dashingwithphase:lengths:transform:).md)
  Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [func copy(strokingWithWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform) -> CGPath](cgpath/copy(strokingwithwidth:linecap:linejoin:miterlimit:transform:).md)
  Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [func mutableCopy() -> CGMutablePath?](cgpath/mutablecopy.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](cgpath/mutablecopy(using:).md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/copy())*