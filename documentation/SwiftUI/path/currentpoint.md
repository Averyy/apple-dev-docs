# currentPoint

**Framework**: SwiftUI  
**Kind**: property

Returns the last point in the path, or nil if the path contains no points.

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
var currentPoint: CGPoint? { get }
```

## See Also

- [var boundingRect: CGRect](path/boundingrect.md)
  A rectangle containing all path segments.
- [var cgPath: CGPath](path/cgpath.md)
  An immutable path representing the elements in the path.
- [func contains(CGPoint, eoFill: Bool) -> Bool](path/contains(_:eofill:).md)
  Returns true if the path contains a specified point.
- [var description: String](path/description.md)
  A description of the path that may be used to recreate the path via `init?(_:)`.
- [var isEmpty: Bool](path/isempty.md)
  A Boolean value indicating whether the path contains zero elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/currentpoint)*