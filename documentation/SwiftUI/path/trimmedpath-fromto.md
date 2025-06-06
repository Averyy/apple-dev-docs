# trimmedPath(from:to:)

**Framework**: SwiftUI  
**Kind**: method

Returns a partial copy of the path.

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
func trimmedPath(from: CGFloat, to: CGFloat) -> Path
```

#### Discussion

The returned path contains the region between `from` and `to`, both of which must be fractions between zero and one defining points linearly-interpolated along the path.

## See Also

- [func applying(CGAffineTransform) -> Path](path/applying(_:).md)
  Returns a path constructed by applying the transform to all points of the path.
- [func offsetBy(dx: CGFloat, dy: CGFloat) -> Path](path/offsetby(dx:dy:).md)
  Returns a path constructed by translating all its points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/trimmedpath(from:to:))*