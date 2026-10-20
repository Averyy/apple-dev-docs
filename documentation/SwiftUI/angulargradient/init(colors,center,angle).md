# init(colors:center:angle:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a conic gradient from a collection of colors that completes a full turn.

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
@export(implementation)
nonisolated init(colors: [Color], center: UnitPoint, angle: Angle = .zero)
```

## See Also

### Creating a full rotation angular gradient
- [init(gradient: Gradient, center: UnitPoint, angle: Angle)](./init%28gradient,center,angle%29.md)
  Creates a conic gradient that completes a full turn.
- [init(stops: [Gradient.Stop], center: UnitPoint, angle: Angle)](./init%28stops,center,angle%29.md)
  Creates a conic gradient from a collection of color stops that completes a full turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/angulargradient/init(colors:center:angle:))*