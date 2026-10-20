# boundingRect

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A rectangle containing all path segments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var boundingRect: CGRect { get }
```

#### Discussion

This is the smallest rectangle completely enclosing all points in the path but not including control points for Bézier curves.

## See Also

### Getting the path’s characteristics
- [var cgPath: CGPath](./cgpath.md)
  An immutable path representing the elements in the path.
- [func contains(CGPoint, eoFill: Bool) -> Bool](./contains%28_,eofill%29.md)
  Returns true if the path contains a specified point.
- [var currentPoint: CGPoint?](./currentpoint.md)
  Returns the last point in the path, or nil if the path contains no points.
- [var description: String](./description.md)
  A description of the path that may be used to recreate the path via `init?(_:)`.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value indicating whether the path contains zero elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/boundingrect)*