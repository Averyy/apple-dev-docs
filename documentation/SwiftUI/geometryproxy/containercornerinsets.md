# containerCornerInsets

**Framework**: SwiftUI  
**Kind**: property

Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var containerCornerInsets: RectangleCornerInsets { get }
```

#### Discussion

```swift
GeometryReader { geometry in
    NavigationTitleView()
        .offset(x: geometry.containerCornerInsets.topLeading.width)
}
```

Container corner inset sizes may not be uniform. For example, on iPadOS and macOS, when the window fills the entire screen without displaying window controls, the inset sizes will always be zero. When that window does display window controls, and the view overlaps the window control area, the corner inset size for the top leading corner will be the size of the overlapping area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/containercornerinsets)*