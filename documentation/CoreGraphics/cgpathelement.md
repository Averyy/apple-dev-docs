# CGPathElement

**Framework**: Core Graphics  
**Kind**: struct

A data structure that provides information about a path element.

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
struct CGPathElement
```

## Topics

### Initializers
- [init(type: CGPathElementType, points: UnsafeMutablePointer<CGPoint>)](cgpathelement/init(type:points:).md)
### Instance Properties
- [var points: UnsafeMutablePointer<CGPoint>](cgpathelement/points.md)
  An array of one or more points that serve as arguments.
- [var type: CGPathElementType](cgpathelement/type.md)
  An element type (or operation).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)](cgpath/apply(info:function:).md)
  For each element in a graphics path, calls a custom applier function.
- [typealias CGPathApplierFunction](cgpathapplierfunction.md)
  Defines a callback function that can view an element in a graphics path.
- [enum CGPathElementType](cgpathelementtype.md)
  The type of element found in a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathelement)*