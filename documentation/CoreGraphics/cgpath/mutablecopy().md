# mutableCopy()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates a mutable copy of an existing graphics path.

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
func mutableCopy() -> CGMutablePath?
```

```c
extern CGMutablePathRefCGPathCreateMutableCopy(CGPathRef path);
```

## Return Value

A new, mutable, copy of the specified path. You are responsible for releasing this object.

## Discussion

You can modify a mutable graphics path by calling the various path geometry functions, such as [`CGPathAddArc`](../cgpathaddarc.md), [`CGPathAddLineToPoint`](../cgpathaddlinetopoint.md), and [`CGPathMoveToPoint`](../cgpathmovetopoint.md).

## See Also

### Copying a Graphics Path
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](./mutablecopy%28using%29.md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/mutablecopy())*