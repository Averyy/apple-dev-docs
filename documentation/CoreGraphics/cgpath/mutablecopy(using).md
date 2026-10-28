# mutableCopy(using:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates a mutable copy of a graphics path transformed by a transformation matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func mutableCopy(using transform: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?
```

```c
extern CGMutablePathRefCGPathCreateMutableCopyByTransformingPath(CGPathRef path, const CGAffineTransform *transform);
```

## Return Value

A new, mutable copy of the specified path transformed by the transform parameter. You are responsible for releasing this object.

## Parameters

- `transform`: A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to all elements of the new path.

## See Also

### Copying a Graphics Path
- [func mutableCopy() -> CGMutablePath?](./mutablecopy%28%29.md)
  Creates a mutable copy of an existing graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/mutablecopy(using:))*