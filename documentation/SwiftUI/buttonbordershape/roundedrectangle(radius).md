# roundedRectangle(radius:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A rounded rectangle shape.

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
static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape
```

## Discussion

Use the [`buttonBorderShape(_:)`](../view/buttonbordershape%28_%29.md) view modifier to apply the shape to bordered buttons within a view hierarchy.

> **Note**: This has no effect on non-widget system buttons in macOS.

## Parameters

- `radius`: The corner radius of the rectangle.

## See Also

### Getting border shapes
- [static let automatic: ButtonBorderShape](./automatic.md)
  A shape that defers to the system to determine an appropriate shape for the given context and platform.
- [static let capsule: ButtonBorderShape](./capsule.md)
  A capsule shape.
- [static let circle: ButtonBorderShape](./circle.md)
  A circular shape.
- [static let roundedRectangle: ButtonBorderShape](./roundedrectangle.md)
  A rounded rectangle shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonbordershape/roundedrectangle(radius:))*