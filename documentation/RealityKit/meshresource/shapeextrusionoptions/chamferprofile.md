# chamferProfile

**Framework**: Realitykit  
**Kind**: property

A path that determines the cross-sectional contour of each chamfered edge.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var chamferProfile: Path? { get set }
```

#### Discussion

> **Note**: If the chamfer profile is `nil`, a circular profile is used.

The chamfer profile needs to satisfy the following conditions:

- The path is nonempty.
- The first point on the path is at (0, 0) and the last point is at (1, 1).
- The value of x along the profile either increases or stays the same. In other words, the profile curve may not wrap back on itself.

To learn more about SwiftUI’s [`Path`](https://developer.apple.com/documentation/SwiftUI/Path) structure, see [`Drawing paths and shapes`](https://developer.apple.com/tutorials/SwiftUI/drawing-paths-and-shapes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/chamferprofile)*