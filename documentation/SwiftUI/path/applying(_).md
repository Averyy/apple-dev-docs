# applying(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a path constructed by applying the transform to all points of the path.

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
func applying(_ transform: CGAffineTransform) -> Path
```

#### Return Value

A new copy of the path with the transform applied to all points.

## Parameters

- `transform`: An affine transform to apply to the path.

## See Also

- [func offsetBy(dx: CGFloat, dy: CGFloat) -> Path](path/offsetby(dx:dy:).md)
  Returns a path constructed by translating all its points.
- [func trimmedPath(from: CGFloat, to: CGFloat) -> Path](path/trimmedpath(from:to:).md)
  Returns a partial copy of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/applying(_:))*