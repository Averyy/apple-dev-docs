# pixelLength

**Framework**: SwiftUI  
**Kind**: property

The size of a pixel on the screen.

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
var pixelLength: CGFloat { get }
```

#### Discussion

This value is usually equal to `1` divided by [`displayScale`](environmentvalues/displayscale.md).

## See Also

- [var isLuminanceReduced: Bool](environmentvalues/isluminancereduced.md)
  A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [var displayScale: CGFloat](environmentvalues/displayscale.md)
  The display scale of this environment.
- [var horizontalSizeClass: UserInterfaceSizeClass?](environmentvalues/horizontalsizeclass.md)
  The horizontal size class of this environment.
- [var verticalSizeClass: UserInterfaceSizeClass?](environmentvalues/verticalsizeclass.md)
  The vertical size class of this environment.
- [enum UserInterfaceSizeClass](userinterfacesizeclass.md)
  A set of values that indicate the visual size available to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/pixellength)*