# copy()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates an immutable copy of a graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy() -> CGPath?
```

```c
extern CGPathRefCGPathCreateCopy(CGPathRef path);
```

## Return Value

A new, immutable copy of the specified path. You are responsible for releasing this object.

## See Also

### Copying a Graphics Path
- [func copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](./copy%28using%29.md)
  Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [func copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](./copy%28dashingwithphase,lengths,transform%29.md)
  Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [func copy(strokingWithWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform) -> CGPath](./copy%28strokingwithwidth,linecap,linejoin,miterlimit,transform%29.md)
  Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [func mutableCopy() -> CGMutablePath?](./mutablecopy%28%29.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](./mutablecopy%28using%29.md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.
- [CGPathCreateCopyByDashingPath](../cgpathcreatecopybydashingpath.md)
  Creates a dashed copy of another path.
- [CGPathCreateCopyByStrokingPath](../cgpathcreatecopybystrokingpath.md)
  Creates a stroked copy of another path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/copy())*