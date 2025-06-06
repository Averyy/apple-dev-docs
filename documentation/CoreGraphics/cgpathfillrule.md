# CGPathFillRule

**Framework**: Core Graphics  
**Kind**: enum

Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](cgcontext/fillpath(using:).md) and [`clip(using:)`](cgcontext/clip(using:).md) methods.

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
enum CGPathFillRule
```

#### Overview

When filling a path, regions that a fill rule defines as interior to the path are painted. When clipping with a path, regions interior to the path remain visible after clipping.

## Topics

### Enumeration Cases
- [CGPathFillRule.evenOdd](cgpathfillrule/evenodd.md)
  A rule that considers a region to be interior to a path based on the number of times it is enclosed by path elements.
- [CGPathFillRule.winding](cgpathfillrule/winding.md)
  A rule that considers a region to be interior to a path if the winding number for that region is nonzero.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum CGTextEncoding](cgtextencoding.md)
  Text encodings for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathfillrule)*