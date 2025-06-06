# ColorRenderingMode.extendedLinear

**Framework**: SwiftUI  
**Kind**: case

The extended linear sRGB working color space.

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
case extendedLinear
```

#### Discussion

Color component values outside the range `[0, 1]` are preserved. This color space isn’t gamma corrected.

## See Also

- [ColorRenderingMode.linear](colorrenderingmode/linear.md)
  The linear sRGB working color space.
- [ColorRenderingMode.nonLinear](colorrenderingmode/nonlinear.md)
  The non-linear sRGB working color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorrenderingmode/extendedlinear)*