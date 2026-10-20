# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A shape that defers to the system to determine an appropriate shape for the given context and platform.

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
static let automatic: ButtonBorderShape
```

#### Discussion

Use the [`buttonBorderShape(_:)`](../view/buttonbordershape%28_%29.md) view modifier to apply the shape to bordered buttons within a view hierarchy.

## See Also

### Getting border shapes
- [static let capsule: ButtonBorderShape](./capsule.md)
  A capsule shape.
- [static let circle: ButtonBorderShape](./circle.md)
  A circular shape.
- [static let roundedRectangle: ButtonBorderShape](./roundedrectangle.md)
  A rounded rectangle shape.
- [static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape](./roundedrectangle%28radius%29.md)
  A rounded rectangle shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonbordershape/automatic)*