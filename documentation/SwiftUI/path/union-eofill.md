# union(_:eoFill:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new path with filled regions in either this path or the given path.

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
func union(_ other: Path, eoFill: Bool = false) -> Path
```

#### Return Value

A new path.

#### Discussion

The filled region of resulting path is the combination of the filled region of both paths added together.

Any unclosed subpaths in either path are assumed to be closed. The result of filling this path using either even-odd or non-zero fill rules is identical.

## Parameters

- `other`: The path to union.
- `eoFill`: Whether to use the even-odd rule for determining   which areas to treat as the interior of the paths (if true),   or the non-zero rule (if false).

## See Also

- [func addRoundedRect(in: CGRect, cornerSize: CGSize, style: RoundedCornerStyle, transform: CGAffineTransform)](path/addroundedrect(in:cornersize:style:transform:).md)
  Adds a rounded rectangle to the path.
- [func intersection(Path, eoFill: Bool) -> Path](path/intersection(_:eofill:).md)
  Returns a new path with filled regions common to both paths.
- [func lineIntersection(Path, eoFill: Bool) -> Path](path/lineintersection(_:eofill:).md)
  Returns a new path with a line from this path that overlaps the filled regions of the given path.
- [func lineSubtraction(Path, eoFill: Bool) -> Path](path/linesubtraction(_:eofill:).md)
  Returns a new path with a line from this path that does not overlap the filled region of the given path.
- [func normalized(eoFill: Bool) -> Path](path/normalized(eofill:).md)
  Returns a new weakly-simple copy of this path.
- [func subtracting(Path, eoFill: Bool) -> Path](path/subtracting(_:eofill:).md)
  Returns a new path with filled regions from this path that are not in the given path.
- [func symmetricDifference(Path, eoFill: Bool) -> Path](path/symmetricdifference(_:eofill:).md)
  Returns a new path with filled regions either from this path or the given path, but not in both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/union(_:eofill:))*