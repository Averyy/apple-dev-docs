# union(_:eoFill:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new shape with filled regions in either this shape or the given shape.

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
func union<T>(_ other: T, eoFill: Bool = false) -> some Shape where T : Shape
```

#### Return Value

A new shape.

#### Discussion

The filled region of resulting shape is the combination of the filled region of both shapes added together.

Any unclosed subpaths in either shape are assumed to be closed. The result of filling this shape using either even-odd or non-zero fill rules is identical.

## Parameters

- `other`: The shape to union.
- `eoFill`: Whether to use the even-odd rule for determining   which areas to treat as the interior of the shapes (if true),   or the non-zero rule (if false).

## See Also

- [func intersection<T>(T, eoFill: Bool) -> some Shape](shape/intersection(_:eofill:).md)
  Returns a new shape with filled regions common to both shapes.
- [func lineIntersection<T>(T, eoFill: Bool) -> some Shape](shape/lineintersection(_:eofill:).md)
  Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [func lineSubtraction<T>(T, eoFill: Bool) -> some Shape](shape/linesubtraction(_:eofill:).md)
  Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [func subtracting<T>(T, eoFill: Bool) -> some Shape](shape/subtracting(_:eofill:).md)
  Returns a new shape with filled regions from this shape that are not in the given shape.
- [func symmetricDifference<T>(T, eoFill: Bool) -> some Shape](shape/symmetricdifference(_:eofill:).md)
  Returns a new shape with filled regions either from this shape or the given shape, but not in both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/union(_:eofill:))*