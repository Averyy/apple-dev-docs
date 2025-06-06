# CGPathElementType

**Framework**: Core Graphics  
**Kind**: enum

The type of element found in a path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGPathElementType
```

#### Overview

For more information about paths, see [`CGPath`](cgpath.md).

## Topics

### Constants
- [CGPathElementType.moveToPoint](cgpathelementtype/movetopoint.md)
  The path element that starts a new subpath.
- [CGPathElementType.addLineToPoint](cgpathelementtype/addlinetopoint.md)
  The path element that adds a line from the current point to a new point.
- [CGPathElementType.addQuadCurveToPoint](cgpathelementtype/addquadcurvetopoint.md)
  The path element that adds a quadratic curve from the current point to the specified point.
- [CGPathElementType.addCurveToPoint](cgpathelementtype/addcurvetopoint.md)
  The path element that adds a cubic curve from the current point to the specified point.
- [CGPathElementType.closeSubpath](cgpathelementtype/closesubpath.md)
  The path element that closes and completes a subpath. The element does not contain any points. See the function [`closeSubpath()`](cgmutablepath/closesubpath().md).
### Initializers
- [init?(rawValue: Int32)](cgpathelementtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)](cgpath/apply(info:function:).md)
  For each element in a graphics path, calls a custom applier function.
- [typealias CGPathApplierFunction](cgpathapplierfunction.md)
  Defines a callback function that can view an element in a graphics path.
- [struct CGPathElement](cgpathelement.md)
  A data structure that provides information about a path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathelementtype)*