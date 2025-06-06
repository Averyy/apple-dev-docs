# isOpaque

**Framework**: SwiftUI  
**Kind**: property

A Boolean that indicates whether the canvas is fully opaque.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isOpaque: Bool { get set }
```

#### Discussion

You might be able to improve performance by setting this value to `true`, making the canvas is fully opaque. However, in that case, the result of drawing a non-opaque image into the canvas is undefined.

## See Also

- [var colorMode: ColorRenderingMode](canvas/colormode.md)
  The working color space and storage format of the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/canvas/isopaque)*