# lineIntersection(_:eoFill:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func lineIntersection<T>(_ other: T, eoFill: Bool = false) -> some Shape where T : Shape
```

#### Return Value

A new shape.

#### Discussion

The line of the resulting shape is the line of this shape that overlaps the filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths that do not intersect `other` remain closed.

## Parameters

- `other`: The shape to intersect.
- `eoFill`: Whether to use the even-odd rule for determining   which areas to treat as the interior of the shapes (if true),   or the non-zero rule (if false).

## See Also

- [func intersection<T>(T, eoFill: Bool) -> some Shape](shape/intersection(_:eofill:).md)
  Returns a new shape with filled regions common to both shapes.
- [func lineSubtraction<T>(T, eoFill: Bool) -> some Shape](shape/linesubtraction(_:eofill:).md)
  Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [func subtracting<T>(T, eoFill: Bool) -> some Shape](shape/subtracting(_:eofill:).md)
  Returns a new shape with filled regions from this shape that are not in the given shape.
- [func symmetricDifference<T>(T, eoFill: Bool) -> some Shape](shape/symmetricdifference(_:eofill:).md)
  Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [func union<T>(T, eoFill: Bool) -> some Shape](shape/union(_:eofill:).md)
  Returns a new shape with filled regions in either this shape or the given shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/lineintersection(_:eofill:))*