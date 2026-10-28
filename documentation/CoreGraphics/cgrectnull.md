# CGRectNull

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

The null rectangle, representing an invalid value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CGRectNull: CGRect
```

```c
extern const CGRect CGRectNull;
```

## Discussion

This is the rectangle returned when, for example, you intersect two disjoint rectangles. Note that the null rectangle is not the same as the [`CGRectZero`](./cgrectzero.md) rectangle. For example, the union of a rectangle with the null rectangle is the original rectangle (that is, the null rectangle contributes nothing).

## See Also

### Constants
- [let CGRectInfinite: CGRect](./cgrectinfinite.md)
  A rectangle that has infinite extent.
- [Geometric Zeros](./geometric-zeros.md)
  A zero point, zero rectangle, or zero size.
- [enum CGRectEdge](../CoreFoundation/cgrectedge.md)
- [CGFloat Informational Macros](./cgfloat-informational-macros.md)
  Informational macros for the `CGFloat` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectnull)*