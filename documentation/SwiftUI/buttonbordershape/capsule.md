# capsule

**Framework**: SwiftUI  
**Kind**: property

A capsule shape.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let capsule: ButtonBorderShape
```

#### Discussion

Use the [`buttonBorderShape(_:)`](view/buttonbordershape(_:).md) view modifier to apply the shape to bordered buttons within a view hierarchy.

> **Note**: This has no effect on non-widget system buttons in macOS.

This has no effect on non-widget system buttons in macOS.

## See Also

- [static let automatic: ButtonBorderShape](buttonbordershape/automatic.md)
  A shape that defers to the system to determine an appropriate shape for the given context and platform.
- [static let circle: ButtonBorderShape](buttonbordershape/circle.md)
  A circular shape.
- [static let roundedRectangle: ButtonBorderShape](buttonbordershape/roundedrectangle.md)
  A rounded rectangle shape.
- [static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape](buttonbordershape/roundedrectangle(radius:).md)
  A rounded rectangle shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonbordershape/capsule)*